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

## Workflow

The following is the general workflow for using the Version Control System (VCS). This section describes the typical steps a user will take to interact with the system, from initializing a repository to managing files, branches, and commits.

### 1. Initialize the Repository

Before starting to track files, you must initialize a new repository.

```bash
$ vcs init
```

#### Internal Workflow:
- A `.vcs` directory is created to store the version control data (including branches, commits, and staging areas).
- A default `main` branch is created.
- A `HEAD` file is created to track the current branch.

### 2. Add Files to Staging Area

To begin tracking a file, use the `add` command to move files to the staging area.

```bash
$ vcs add <file_name>
```

#### Internal Workflow:
- The system checks if the file exists and if it’s not listed in the `.vcs/ignore` file.
- The file is copied from the working directory into the `.vcs/staging/` directory.

### 3. Commit Changes

Once the files are staged, commit them to record the changes.

```bash
$ vcs commit -m "Commit message"
```

#### Internal Workflow:
- The system verifies that there are staged files in the `staging/` directory.
- A new commit directory is created within the current branch’s directory.
- The commit message is saved in the commit directory.
- The files in the staging area are copied to the commit directory.

### 4. View Commit History

To view the commit history of the current branch, use the `log` command.

```bash
$ vcs log
```

#### Internal Workflow:
- The system reads the commit directories from the current branch’s directory.
- It displays each commit ID along with the associated commit message.

### 5. Switching Branches

You can create and switch between branches with the `branch` and `checkout` commands.

```bash
$ vcs branch <new_branch_name>     # Create a new branch
$ vcs checkout <branch_name>       # Switch to a branch
```
The `merge` command merges changes from another branch into the current branch.
#### Internal Workflow:
- The system creates a new directory for the new branch inside the `branches/` directory.
- The `HEAD` file is updated to reflect the new branch.
- When switching branches, the files from the newly checked-out branch are loaded, replacing the files in the working directory.

### 6. Merging Branches

To merge changes from another branch into your current branch, use the `merge` command.

```bash
$ vcs merge <branch_name>
```

#### Internal Workflow:
- The system copies the commit history from the target branch into the current branch’s directory.
- Any missing commits from the target branch are added to the current branch.
- In case of conflicts, the user will be prompted to resolve them manually (currently, the system uses symlinks for simplicity).

### 7. Ignore Files

To prevent certain files from being tracked by the VCS, use the `ignore` command to specify file patterns.

```bash
$ vcs ignore <file_pattern>
```

#### Internal Workflow:
- The system appends the file pattern to the `.vcs/ignore` file.
- Files matching the pattern will be skipped during the `add` process.

### 8. Cloning a Repository

To create a copy of an existing repository, use the `clone` command.

```bash
$ vcs clone <repository_path> <new_repository_path>
```

#### Internal Workflow:
- The system copies all files and directories from the source repository to the destination path.
- It ensures the `.vcs` structure is preserved, allowing the cloned repository to function independently.

### 9. Viewing Differences Between Commits

To see the changes between two commits, use the `diff` command.

```bash
$ vcs diff <commit_id1> <commit_id2>
```

#### Internal Workflow:
- The system retrieves the files from both commits and compares them.
- The differences are displayed using a unified diff format.

### Example Workflow

Here’s an example of how you might use the VCS to track changes in a project:

1. **Initialize the repository**:
    ```bash
    $ vcs init
    ```

2. **Create and add files**:
    ```bash
    $ echo "Hello, world!" > hello.txt
    $ vcs add hello.txt
    ```

3. **Commit the changes**:
    ```bash
    $ vcs commit -m "Add hello.txt file"
    ```

4. **Create a new branch and switch to it**:
    ```bash
    $ vcs branch feature-branch
    $ vcs checkout feature-branch
    ```

5. **Modify a file and add it**:
    ```bash
    $ echo "New feature added!" > feature.txt
    $ vcs add feature.txt
    ```

6. **Commit the changes**:
    ```bash
    $ vcs commit -m "Add feature.txt file"
    ```

7. **Switch back to the main branch and merge the changes**:
    ```bash
    $ vcs checkout main
    $ vcs merge feature-branch
    ```

This simple workflow demonstrates how to track changes, create branches, and merge them in a VCS system.

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
