import os
import sys
import argparse
from difflib import unified_diff
import cmd
import shutil

class VCS:
    def __init__(self):
        self.repo_dir = ".vcs"

    def init(self):
        """Initialize a new repository."""
        if os.path.exists(self.repo_dir):
            print("Repository already initialized.")
            return
        os.makedirs(os.path.join(self.repo_dir, "commits"))
        os.makedirs(os.path.join(self.repo_dir, "branches"))
        open(os.path.join(self.repo_dir, "ignore"), "w").close()
        open(os.path.join(self.repo_dir, "HEAD"), "w").write("main")
        print("Initialized empty VCS repository.")

    def add(self, file_path):
        """Stage a file for the next commit."""
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return

        ignore_file = os.path.join(self.repo_dir, "ignore")
        if os.path.isfile(ignore_file):
            with open(ignore_file) as f:
                ignored_files = f.read().splitlines()
            if any(file_path.endswith(ignored) for ignored in ignored_files):
                print(f"File '{file_path}' is ignored.")
                return

        staging_path = os.path.join(self.repo_dir, "staging")
        os.makedirs(staging_path, exist_ok=True)
        destination = os.path.join(staging_path, os.path.basename(file_path))
        with open(file_path, "r") as src, open(destination, "w") as dest:
            dest.write(src.read())
        print(f"File '{file_path}' added to staging area.")

    def commit(self, message):
        """Create a new commit with the staged files."""
        staging_path = os.path.join(self.repo_dir, "staging")
        if not os.path.exists(staging_path) or not os.listdir(staging_path):
            print("Error: No files staged for commit.")
            return

        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, "branches", branch)
        os.makedirs(branch_path, exist_ok=True)

        commit_id = str(len(os.listdir(branch_path))).zfill(4)
        commit_path = os.path.join(branch_path, commit_id)
        os.makedirs(commit_path)

        for file in os.listdir(staging_path):
            src = os.path.join(staging_path, file)
            dest = os.path.join(commit_path, file)
            with open(src, "r") as s, open(dest, "w") as d:
                d.write(s.read())

        with open(os.path.join(commit_path, "message"), "w") as f:
            f.write(message)

        for file in os.listdir(staging_path):
            os.remove(os.path.join(staging_path, file))
        print(f"Commit {commit_id} created on branch '{branch}' with message: {message}")

    def log(self):
        """Display the commit history."""
        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, "branches", branch)

        if not os.path.exists(branch_path) or not os.listdir(branch_path):
            print("No commits yet.")
            return

        for commit_id in sorted(os.listdir(branch_path), reverse=True):
            commit_path = os.path.join(branch_path, commit_id)
            with open(os.path.join(commit_path, "message"), "r") as f:
                print(f"Commit {commit_id}: {f.read().strip()}")

    def diff(self, commit1, commit2):
        """Show differences between two commits."""
        branch = self.get_current_branch()
        branch_path = os.path.join(self.repo_dir, "branches", branch)
        path1 = os.path.join(branch_path, commit1)
        path2 = os.path.join(branch_path, commit2)

        if not os.path.exists(path1) or not os.path.exists(path2):
            print("Error: One or both commits do not exist.")
            return

        files1 = {f: open(os.path.join(path1, f)).read() for f in os.listdir(path1) if f != "message"}
        files2 = {f: open(os.path.join(path2, f)).read() for f in os.listdir(path2) if f != "message"}

        all_files = set(files1.keys()).union(files2.keys())
        for file in all_files:
            content1 = files1.get(file, "").splitlines()
            content2 = files2.get(file, "").splitlines()
            diff = unified_diff(content1, content2, fromfile=f"{commit1}/{file}", tofile=f"{commit2}/{file}")
            print("\n".join(diff))

    def branch(self, branch_name):
        """Create a new branch."""
        branch_path = os.path.join(self.repo_dir, "branches", branch_name)
        if os.path.exists(branch_path):
            print(f"Branch '{branch_name}' already exists.")
            return

        current_branch = self.get_current_branch()
        current_branch_path = os.path.join(self.repo_dir, "branches", current_branch)

        os.makedirs(branch_path)
        for commit in os.listdir(current_branch_path):
            src = os.path.join(current_branch_path, commit)
            dest = os.path.join(branch_path, commit)
            
        if os.path.isdir(src):
            shutil.copytree(src, dest)
        else:
            shutil.copy(src, dest)

        print(f"Branch '{branch_name}' created.")

    def checkout(self, branch_name):
        """Switch to a different branch."""
        branch_path = os.path.join(self.repo_dir, "branches", branch_name)
        if not os.path.exists(branch_path):
            print(f"Branch '{branch_name}' does not exist.")
            return

        with open(os.path.join(self.repo_dir, "HEAD"), "w") as f:
            f.write(branch_name)
        print(f"Switched to branch '{branch_name}'.")

    def get_current_branch(self):
        """Get the name of the current branch."""
        head_path = os.path.join(self.repo_dir, "HEAD")
        if os.path.exists(head_path):
            with open(head_path, "r") as f:
                return f.read().strip()
        return "main"

    def merge(self, target_branch):
        """Merge another branch into the current branch."""
        current_branch = self.get_current_branch()
        current_branch_path = os.path.join(self.repo_dir, "branches", current_branch)
        target_branch_path = os.path.join(self.repo_dir, "branches", target_branch)

        if not os.path.exists(target_branch_path):
            print(f"Error: Branch '{target_branch}' does not exist.")
            return

        target_commits = sorted(os.listdir(target_branch_path))
        current_commits = sorted(os.listdir(current_branch_path))

        for commit in target_commits:
            if commit not in current_commits:
                src = os.path.join(target_branch_path, commit)
                dest = os.path.join(current_branch_path, commit)
                os.symlink(src, dest)

        print(f"Branch '{target_branch}' merged into '{current_branch}'.")

    def ignore(self, pattern):
        """Add a file pattern to ignore."""
        ignore_file = os.path.join(self.repo_dir, "ignore")
        with open(ignore_file, "a") as f:
            f.write(f"{pattern}\n")
        print(f"Pattern '{pattern}' added to ignore file.")

    def clone(self, destination):
        """Clone the repository to a new location."""
        if os.path.exists(destination):
            print(f"Error: Destination '{destination}' already exists.")
            return

        os.makedirs(destination)
        for root, dirs, files in os.walk(self.repo_dir):
            rel_path = os.path.relpath(root, self.repo_dir)
            target_dir = os.path.join(destination, rel_path)
            os.makedirs(target_dir, exist_ok=True)

            for file in files:
                src = os.path.join(root, file)
                dest = os.path.join(target_dir, file)
                with open(src, "r") as s, open(dest, "w") as d:
                    d.write(s.read())

        print(f"Repository cloned to '{destination}'.")

class VCSCmd(cmd.Cmd):
    intro = "Welcome to the VCS shell. Type help or ? to list commands.\n"
    prompt = "(vcs) "
    vcs = VCS()

    def do_init(self, arg):
        "Initialize a new repository: init"
        self.vcs.init()

    def do_add(self, arg):
        "Stage a file for the next commit: add <file_path>"
        self.vcs.add(arg)

    def do_commit(self, arg):
        "Create a new commit with the staged files: commit <message>"
        self.vcs.commit(arg)

    def do_log(self, arg):
        "Display the commit history: log"
        self.vcs.log()

    def do_diff(self, arg):
        "Show differences between two commits: diff <commit1> <commit2>"
        args = arg.split()
        if len(args) != 2:
            print("Error: Missing commit IDs.")
        else:
            self.vcs.diff(args[0], args[1])

    def do_branch(self, arg):
        "Create a new branch: branch <branch_name>"
        self.vcs.branch(arg)

    def do_checkout(self, arg):
        "Switch to a different branch: checkout <branch_name>"
        self.vcs.checkout(arg)

    def do_merge(self, arg):
        "Merge another branch into the current branch: merge <branch_name>"
        self.vcs.merge(arg)

    def do_ignore(self, arg):
        "Add a file pattern to ignore: ignore <pattern>"
        self.vcs.ignore(arg)

    def do_clone(self, arg):
        "Clone the repository to a new location: clone <destination>"
        self.vcs.clone(arg)

    def do_exit(self, arg):
        "Exit the VCS shell: exit"
        print("Exiting...")
        return True

if __name__ == "__main__":
    VCSCmd().cmdloop()
