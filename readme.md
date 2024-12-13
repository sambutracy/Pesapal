# Version Control System (VCS)

## Introduction

This Version Control System (VCS) is a custom implementation designed to manage and track file changes within a repository. It includes key functionalities such as file staging, commit tracking, branch management, and merging, similar to traditional VCS tools like Git. The system is implemented in Python. It offers a command-line interface for users to interact with the repository.

## Project Structure

The VCS is structured around a repository that contains several key directories and files:

.vcs/
├── branches/ # Stores the different branches and commits for each branch.
│   ├── main/ # Main branch containing commit history.
│   └── <branch_name>/ # Other branches with their respective commits.
├── commits/ # Stores commit information (currently not in use).
├── ignore/ # Stores ignored file patterns.
- **`HEAD`**: Stores the name of the current active branch.
└── staging/ # Temporary storage for files to be committed.

### Key Components:
- `branches/`: Contains subdirectories for each branch (e.g., `main`, `feature_branch`), where each subdirectory holds commits for that branch.
- `commits/`: A directory that can store detailed information about commits (optional).
- `ignore/`: Stores file patterns to ignore during staging, such as temporary or build files.
- `HEAD`: A file indicating the current branch.
- `staging/`: A temporary directory where files are placed before they are committed.

## VCS Functionalities

### 1. Initialization (`init`)

The `init` command initializes a new repository by creating the `.vcs` directory, which contains all the necessary subdirectories and files for version control, including initializing the `ignore` file. If the repository is already initialized, an appropriate message is displayed.

#### Process:
- Creates the `.vcs` directory.
- Creates `branches/`, `commits/`, and `staging/` directories.
- Initializes a file named `HEAD`, which stores the current active branch (defaults to `main`).
- Initializes an empty `ignore` file to store ignored file patterns.

### 2. Adding Files (`add`)

The `add` command stages files for the next commit. This involves copying the files from the working directory to the staging area.

#### Process:
- The system checks if the file exists.
- It checks the `ignore` file to ensure the file is not excluded from version control.
- If not ignored, the file is copied to the `staging/` directory, ready for commit.

### 3. Committing Changes (`commit`)

The `commit` command creates a new commit with all staged files, storing them in the current branch's history. A commit message is required and provided as an argument, which is saved alongside the files.

#### Process:
- The system checks if there are staged files in the `staging/` directory.
- If no files are staged, it returns an error.
- The commit files are copied from the staging area to a new commit directory within the current branch’s directory.
- A commit message is saved in the newly created commit directory.

### 4. Viewing Commit History (`log`)

The `log` command displays the commit history of the current branch, showing each commit’s ID and message.

#### Process:
- Reads the commit history from the current branch's directory.
- Displays commit IDs and associated messages.

### 5. Showing Differences Between Commits (`diff`)

The `diff` command shows the changes between two commits and displays the differences between them. It uses the unified diff format to show any changes in the files between the two commits.

#### Process:
- Retrieves the files from both commits.
- Compares the file content using the `unified_diff` method from Python's `difflib` library.
- Displays the differences for each file that has changed.

### 6. Branch Management

#### Creating a Branch (`branch`)

The `branch` command creates a new branch by copying the commit history from the current branch. If the branch already exists, an error is raised.

#### Switching Branches (`checkout`)

The `checkout` command switches to a different branch. It updates the `HEAD` file to indicate the new current branch.

#### Merging Branches (`merge`)

The `merge` command merges changes from another branch into the current branch. It copies any missing commits from the target branch to the current branch’s history.

### 7. Ignoring Files (`ignore`)

The `ignore` command allows users to specify file patterns that should be excluded from tracking by the VCS. This command prevents certain files from being tracked by the VCS, and these files are ignored during the staging process.

#### Process:
- The file pattern is appended to the `ignore` file.
- Any file matching the pattern is skipped during the `add` operation.

### 8. Cloning a Repository (`clone`)

The `clone` command creates a copy of an existing repository in a new location. This includes all branches, commits, and other necessary files.

#### Process:
- The system copies all files and directories from the source repository to the new destination.
- It replicates the `.vcs` structure, ensuring the new repository functions independently.

Here’s an updated version of the workflow with the first step to run the `vcs.py` script in interactive mode using `python -i vcs.py`:

```markdown
## VCS Workflow

This is a simple command-line version control system (VCS) that allows you to manage your files, create branches, and make commits in a repository. Below is the workflow to help you get started with using the VCS.

### 1. Run the VCS Script

Before you can use the VCS commands, you need to start the Python script in interactive mode. You can do this by running the following command:

```bash
python -i vcs.py
```

This will start an interactive Python session with the VCS commands available. You can now execute the available commands in the VCS.

### 2. Initialize the Repository

To create a new repository, use the `init` command. This will initialize a `.vcs` directory that contains all the necessary files for version control.

```bash
vcs> init
```

This will create the following structure in your project:
- `.vcs/commits/` – stores commits
- `.vcs/branches/` – stores branches
- `.vcs/ignore` – lists patterns of files to ignore
- `.vcs/HEAD` – stores the current branch (default is `main`)

### 3. Add Files to Staging

Once the repository is initialized, you can add files to the staging area. The `add` command copies the file into the staging area so that it can be committed later.

```bash
vcs> add <file>
```

You can check if the file has been successfully added by inspecting the `staging/` directory.

### 4. Commit Changes

After staging the files, you can commit the changes. Use the `commit` command to create a new commit with a descriptive message. This command will save all staged files into the current branch's commit history.

```bash
vcs> commit "<msg>"
```

Each commit is stored with a unique ID, and you can view the commit history using the `log` command.

### 5. View Commit History

To view the commit history of the current branch, use the `log` command. This will list all commits made on the current branch, with their commit IDs and associated messages.

```bash
vcs> log
```

### 6. Compare Commits

You can compare two commits to see what changed between them using the `diff` command. This will display a unified diff between the two commits.

```bash
vcs> diff <c1> <c2>
```

### 7. Create a New Branch

To create a new branch, use the `branch` command followed by the name of the new branch. This will copy the current commit history to the new branch.

```bash
vcs> branch <name>
```

### 8. Switch Branches

To switch to a different branch, use the `checkout` command. This will update the `HEAD` file and set the current branch to the one you specify.

```bash
vcs> checkout <branch>
```

### 9. Merge Branches

If you want to merge another branch into your current branch, use the `merge` command. This will bring over commits from the target branch to the current branch.

```bash
vcs> merge <branch>
```

### 10. Ignore Files

You can add file patterns to the ignore list, which will prevent certain files from being staged or committed. Use the `ignore` command followed by the file pattern.

```bash
vcs> ignore <file_pattern>
```

Example:
```bash
vcs> ignore "*.log"
```

### 11. Clone the Repository

If you want to clone the repository to a different location, use the `clone` command. This will copy the entire repository to a new directory.

```bash
vcs> clone <destination>
```

### Summary of Commands

| Command       | Description                                             |
|---------------|---------------------------------------------------------|
| `init`        | Initialize a new repository                            |
| `add <file>`  | Stage a file for commit                                |
| `commit <msg>`| Commit staged changes                                  |
| `log`         | View commit history                                    |
| `diff <c1> <c2>`| View the differences between two commits              |
| `branch <name>`| Create a new branch                                   |
| `checkout <branch>`| Switch to another branch                           |
| `merge <branch>`| Merge a branch into the current branch                |
| `ignore <pattern>`| Add a file pattern to the ignore list                |
| `clone <destination>`| Clone the repository to a new directory           |

With this workflow, you can effectively manage your project files, keep track of changes, and work with multiple branches in your version control system.
```

This ensures that users know how to first start the Python script in interactive mode, and then proceed with the rest of the workflow to manage the repository.

## Design Decisions

### 1. Simplicity
The system is designed to be simple and minimalistic, with an emphasis on understanding core VCS concepts. It avoids complex features like conflict resolution, rebasing, or stashing, focusing instead on the basic functionalities of a VCS.

### 2. File-Based History
Commits are stored as separate directories with file contents copied from the staging area. This approach allows for easy tracking of changes but lacks advanced features like delta compression or object databases found in Git.

### 3. Branching and Merging
Branching is done by copying the commit history from the current branch. Merging is handled by copying commits from the target branch into the current branch’s directory. This process could be optimized with more advanced merge algorithms and conflict resolution mechanisms.

### 4. Symlinks in Merging
The merging functionality uses symlinks to link commits from other branches. This approach simplifies the merge process but could lead to issues if file changes are complex, requiring more sophisticated merge strategies.

### 5. Command-Line Interface
The VCS uses a Python `cmd` module-based shell for interaction. This interface makes it easy to extend and add new features while keeping the experience simple for users familiar with the command line.

## Future Improvements

1. **Conflict Resolution**: Implement automatic or manual conflict resolution during the `merge` process.
2. **Efficient Storage**: Use more advanced techniques for storing file changes, such as Git-style object databases, to improve performance and reduce redundancy.
3. **Graphical User Interface (GUI)**: Add a GUI to make the system more accessible to users who are not familiar with command-line interfaces.
4. **Remote Repositories**: Implement support for remote repositories (e.g., GitHub, GitLab) to allow for collaboration across multiple users.

## Conclusion

This VCS implementation serves as a simple, educational version control system that provides the core functionalities necessary for file tracking, branching, and collaboration. While it is not as feature-rich as more established systems like Git, it offers an excellent learning tool for understanding version control mechanics.
