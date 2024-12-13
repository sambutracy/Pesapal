# Distributed Version Control System (VCS)

## Overview

This repository contains a simple Distributed Version Control System (VCS) implemented in Python. It mimics the basic functionalities of Git, allowing users to initialize repositories, stage files, commit changes, view commit history, create branches, merge branches, perform diffs, and ignore files. This project is designed for educational purposes to demonstrate the core principles of version control systems in a distributed environment.

Although features like conflict resolution and rebasing are not implemented, this VCS provides the essential functionality needed to manage code versions across multiple collaborators.

## Problem Context

Version control systems (VCS) like Git are essential tools for software development. They help developers manage changes to code, track revisions, collaborate effectively, and maintain the integrity of codebases. This project aims to demonstrate the core concepts behind distributed version control systems through a simple, easy-to-understand implementation, which serves as a great starting point for understanding the inner workings of tools like Git.


## Features

- **Initialize Repository**: Create a new version control repository in the current directory.
- **Stage Files**: Add files to the staging area to prepare them for committing.
- **Commit Changes**: Save staged changes to the repository with a commit message.
- **View Commit History**: Display the list of commits made to the repository.
- **Create Branches**: Create branches from the main codebase.
- **Merge Branches**: Merge changes from one branch into another.
- **Diffs**: Show differences between commits or branches.
- **Ignore Files**: Specify files that should not be tracked by the VCS.
- **Clone Repository**: Clone a repository from a local directory (disk-based, not over a network).

## Requirements

- Python 3.7+
- Basic understanding of version control systems like Git.

## Setup Instructions

### Cloning the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/sambutracy/Pesapal.git
cd vcs
```

### Running the VCS

Make sure you have Python 3.7 or higher installed. Navigate to the directory where your `vcs.py` file is located. Run the system in interactive mode by executing:

```bash
python -i vcs.py
```

This will launch an interactive Python session where you can begin using the VCS commands.

## Usage Guide

### 1. Initializing a Repository

To initialize a new repository in the current directory:

```python
vcs.init()
```

This will create a `.vcs` directory to store the repository’s metadata.

### 2. Staging Files

To stage a file for committing, use the following command:

```python
vcs.add("filename.txt")
```

You can add multiple files by passing them as arguments:

```python
vcs.add("file1.txt", "file2.txt")
```

### 3. Committing Changes

Once your files are staged, you can commit the changes with a message:

```python
vcs.commit("Initial commit")
```

This will create a new commit in the repository with the specified commit message.

### 4. Viewing Commit History

To view the commit history, use:

```python
vcs.log()
```

This will display the list of all commits, including the commit hash and associated messages.

### 5. Creating a Branch

To create a new branch from the current commit:

```python
vcs.branch("new-branch")
```

### 6. Merging Branches

To merge a branch into the current one, use:

```python
vcs.merge("new-branch")
```

If there are conflicts, they will be detected, but there will be no automatic resolution—manual intervention is required.

### 7. Diffing Between Commits

To view the differences between two commits, use:

```python
vcs.diff(commit_hash_1, commit_hash_2)
```

This will show the differences between the two specified commits.

### 8. Ignoring Files

To ignore files in the repository (i.e., prevent them from being staged or committed), use:

```python
vcs.ignore("filename.txt")
```

These files will not be tracked by the VCS.

### 9. Cloning a Repository

To clone a repository from a local directory:

```python
vcs.clone("/path/to/existing/repository")
```

This will create a copy of the repository in the current directory.

## How the System Works

The system stores metadata in a `.vcs` directory in each repository. The directory contains:

- `commits/`: A folder containing commit objects with file changes and metadata.
- `branches/`: A folder containing information about branch heads.
- `staging/`: A folder containing files staged for the next commit.
- `ignore/`: A file containing a list of files to ignore.

When you commit changes, the system generates a new commit object, stores it in the `commits/` directory, and updates the branch head. Staging adds files to the `staging/` directory. When committing, the staged files are copied to the commit object.


## Code Structure

- `vcs.py`: The main file containing all the VCS logic, including functions for initializing repos, staging files, committing, and more.
- `.vcs/`: A hidden directory where the version control metadata is stored.
    - `commits/`: Stores commit objects.
    - `branches/`: Stores branch information.
    - `staging/`: Stores staged files.
    - `ignore/`: Lists files to ignore.

## Design Decisions

- Simplification: This implementation focuses on the core functionalities (staging, committing, branching, and merging) while omitting more advanced Git features like rebase and conflict resolution. The aim is to provide an educational, easy-to-understand version control system.
- Disk-based Cloning: The system supports cloning repositories from local directories but does not yet include network-based cloning or remote repository management.


## Testing Strategy
This implementation includes basic unit tests for core functionalities such as commit handling, branch creation, and file staging. These tests ensure that key actions work as expected.

Future versions will include more comprehensive tests, especially for scenarios involving merges and diffing between branches.

## Performance Considerations
Currently, the system is optimized for simplicity rather than performance. As the project grows, we plan to introduce optimizations such as incremental diffs and better file management to improve efficiency when working with large repositories.

## Security Considerations
At this stage, security features such as commit data encryption or secure branch handling have not been implemented. Future versions could address these concerns to improve data integrity and prevent unauthorized access to repository metadata.

## Scalability
As this VCS handles repositories of increasing size, future enhancements will focus on storage efficiency and performance. Features like delta encoding for commit objects and optimized memory handling for large repositories are potential areas for improvement.


## Future Improvements

The current implementation is a basic version control system and lacks advanced features such as:

- **Conflict resolution**: When merging branches, conflicts are detected, but no automated conflict resolution exists.
- **Rebasing**: The ability to rebase branches onto a different branch is not implemented.
- **Network support**: Currently, the system only supports disk-based cloning, not remote repositories.

In future versions, these features can be added to enhance the functionality and mimic more advanced systems like Git.


## Contributing

If you'd like to contribute to the project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Submit a pull request.
