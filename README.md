# pre-commit-hooks
python pre-commit hooks

## inject-issue-name

Hook to insert issue identity part from branch name into commit-message  
if commit message does not contain issue identity already. 

Install:
```
pip install pre-commit
pre-commit install --hook-type prepare-commit-msg
```

Example:

branch name ==> `feature/61235-enable-authentication`  
original commit message ==> `authentication enabled by default`  
modified commit message ==> `authentication enabled by default #61235`  
