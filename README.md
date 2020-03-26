# pre-commit-hooks
python pre-commit hooks

## inject-issue-name

This hook inserts issue name part from branch name into end of commit-message

Example:

branch name ==> `feature/61235-enable-authentication`  
original commit message ==> `authentication enabled by default`  
modified commit message ==> `authentication enabled by default #61235`    
