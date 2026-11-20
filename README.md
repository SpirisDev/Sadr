# Sadr

A Python package publishing framework, cause I find package releasing very boring
so I made a automation... Thank me later

## Installation

```
pip install sadr
```

## Usage for PyPI Upload

```python
from sadr import PyPI

# You have to add the directory here, so Sadr can find the package
sadr = PyPI(".")

# This validates if you have the files required for a release
sadr.val()

# This will build the wheel and distribution files and folders
sadr.build()

# This returns data about the dist/ directory
sadr.inspect()

# This checks if you have twine
sadr.check_twine()

# This will check if the package is right and all things work
sadr.check()

# This will release your package, you have to enter the PyPI token
# Don't worry, I won't steal your token :)

sadr.upload(token="__token_here__")
```

## Usage for Github Upload

```python
from sadr import GitHub

"""
First argument: what git executable to use, "git" for most
people, but sometimes it may be named different...
You can even use the path as such:
c = GitHub(r"Idk\git.exe")

Second argument: the path to the folder or leave empty for root folder
"""
sadr = GitHub(git, path)

# This checks if Git exists on your system
sadr.check_git()

# This will initialize git to your folder (git init)
sadr.git_init()

# This will add all your files (git add .)
sadr.git_add()

# This will commit your additions with a message
sadr.commit(msg)

# This will connect Github to your comuter using the remote origin thing
sadr.remote(url)

# This pushes changes to main aka on Github
sadr.push()

# This just does all of that in one go
sadr.upload(url, commit_msg)
```

---
