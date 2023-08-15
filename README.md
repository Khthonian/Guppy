# Guppy
A Discord bot created to help a friend, which outputs basic git commands and relevant descriptions. This is designed to be run on Replit.

## Usage
### List Available Commands
```
/guppy all
```

### Give Command Description
```
/guppy command [command]
```

## Git Commands

1. `git init`: Initialises a new Git repository in the current directory.

2. `git clone <repository_ssh>`: Creates a local copy of a remote repository.

3. `git status`: Shows the current state of the repository, including modified files and untracked files.

4. `git add <file>` or `git add .`: Adds changes in the working directory to the staging area (index) for the next commit.

5. `git add -A`: Adds all changes, including modifications, deletions, and new files, to the staging area.

6. `git reset <file>`: Unstages changes for a specific file, removing it from the staging area.

7. `git commit`: Records changes from the staging area into the Git history. You'll need to provide a commit message in a text editor, in your case, VS Code.

8. `git commit -m "Your commit message"`: Creates a commit with a commit message in a single command, bypassing the text editor.

9. `git log`: Displays the commit history, showing the author, date, and commit message.

10. `git diff`: Shows the changes made to the files in the working directory compared to the last commit.

11. `git pull`: Fetches and merges changes from the remote repository into the current branch.

12. `git push`: Sends local commits to the remote repository. Reserve this for when you're on the main branch, to be safe.

13. `git push <remote> <branch>`: Pushes the specified branch to the specified remote repository; this is the safest way to push in my opinion, even on the main branch. The remote is typically origin, although there are more details we can go into on this.

14. `git branch`: Lists all local branches and marks the current branch with an asterisk.

15. `git branch <branch_name>`: Creates a new branch with the given name. Less preferable to `git checkout -b <branch_name>` in my opinion.

16. `git branch -d <branch_name>`: Deletes a specific branch.

17. `git checkout <branch_name>`: Switches to the specified branch.

18. `git checkout -b <branch_name>`: Creates a new branch and switches to it.

19. `git merge <branch_name>`: Merges the specified branch into the current branch. Must be executed from within the branch you wish to **merge into**.

20. `git remote`: Lists all remote repositories linked to the current repository.

21. `git remote add <remote_name> <repository_url>`: Adds a new remote repository with the specified name and URL.

22. `git remote remove <remote_name>`: Removes the specified remote repository from the list of remotes.

23. `git remote -v`: Displays detailed information about the remote repositories.

24. `git fetch`: Retrieves changes from the remote repository without merging them into the current branch.

25. `git stash`: Temporarily stores changes that are not ready for a commit.

26. `git stash apply`: Applies the most recent stash and leaves it in the stash list.

27. `git stash pop`: Applies the most recent stash and removes it from the stash list.

28. `git stash list`: Lists all the stashes that have been created.

29. `git tag`: Lists all the tags in the repository.

30. `git tag <tag_name>`: Creates a new lightweight tag at the current commit.

31. `git tag -a <tag_name> -m "Tag message"`: Creates an annotated tag with a message.
