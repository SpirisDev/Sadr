## Usage for PyPI Upload

```python
from sadr import PyPI_Up

# You have to add the directory here, so Sadr can find the package
sadr = PyPI_Up(".")

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

"""
Now PyPI_Manage, its for managing projects in PyPI
"""

from sadr import PyPI_Manage

# You add the path here
pm = PyPI_Manage(path)

# This will install the package you named
pm.install(pkg_name)

# This gets the documentation for the named package
pm.get_package(pkg_name)

# This gets the versions available
pm.get_versions(pkg_name)

# This gets the information about the latest pkg
pm.get_latest(pkg_name)

# This gets the information about the version
pm.get_release(pkg_name)

# This deletes the build binaries of PyPI
pm.delete_local()

# This checks if the package exists
pm.check_name(pkg_name)

# This gets the download count using pypistats.org API
# It supports 3 time frames: month, week, day
pm.get_downloads(pkgname, time_period)
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

# This pulls a repo into a folder
sadr.pull(remote="origin", branch="main", rebase=True)

# This logs the output
sadr.log(count=10)

# Creates a new branch for use
sadr.create_branch(name)

# Switches the active branch
sadr.switch(name)

# Deletes a branch
sadr.delete_branch(name)

# Clones a repo into a folder
# Default path is root
sadr.clone(url, path=None)
```

## Usage for Release

```python
from sadr import Release

# This function is for doing all functions at once
# Update PyPI and GitHub in one go

r = Release("Sadr")

# This is for credentials and metadata
creds = {
    """ Used for uploading to GitHub """
    "commit_msg": commit_msg,
    """ Remote origin url, link your repository """
    "url": url,
    """ PyPI Token for uploading to PyPI """
    "pypi_token": pypi_token
}

# Releases the code with automation with the credentials provided
r.release(creds)

"""
Also has a mode for creation of `setup.py`
"""

from sadr import Setup

# directory, file_name, defaulted to:
# . (root) , setup.py
s = Setup(dir, file)

""" enc is for encoding, defaulted to utf-8, for nearly all functions and is optional """

# Imports and opening the function
s.start()

# Name, Version and Description metadata
s.metadata(name, version, desc, enc)

# Inserts the ending bracket
s.end(enc)

# Adds long description README.md
# Not defaulted to `README.md`
s.long_desc(file, enc)

# Specifies the type of desc, defaulted to text/md
s.long_desc_type(type, enc)

# Adds packages, defaulted to find_packages()
s.packages(pack, enc)

# Adds the requires python list, defaulted to ">=3.8"
s.py_requires(ver, enc)

# Install requirements
s.install_req(text, enc)

# Classifiers, for specifying your project
s.classifier(clss, enc)

# Keywords, again, for specifying your project
# Defaulted to "pypi"
s.keywords(keyw, enc)
```

## Cool stuff

I update `Sadr` using `Sadr`... Self-hosting at its peak. Please share the project with your coder friends!
Thanks!

---
