from pathlib import Path
from sadr.pypi import PyPI_Up, PyPI_Manage
from sadr.github import GitHub

class Setup():
    def __init__(self, dir=".", file="setup.py"):
        self.dir = Path(dir).resolve()
        self.file = Path(file)

    def start(self):
        self.file.write_text("from setuptools import setup, find_packages\nfrom pathlib import Path\n\nsetup(\n")

    def metadata(self, name, version, desc, enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""name="{name}",\nversion="{version}",\ndescription="{desc}",\n""", encoding=enc)

    def end(self, enc="utf-8"):
        self.file.write_text(self.file.read_text() + "\n)", encoding=enc)

    def long_desc(self, file, enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""long_description=Path("{file}").read_text(encoding="{enc}"),\n""")

    def long_desc_type(self, type="text/markdown", enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""long_description_content_type="{type}",\n""", encoding=enc)

    def packages(self, pack="find_packages()", enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"packages={pack},\n", encoding=enc)

    def py_requires(self, ver=">=3.8", enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""python_requires="{ver}",\n""")

    def install_req(self, text, enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""install_requires=["{text}"],\n""", encoding=enc)

    def classifier(self, clss, enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"classifiers={clss},\n", encoding=enc)

    def keywords(self, keyw="pypi", enc="utf-8"):
        self.file.write_text(self.file.read_text() + f"""keywords="{keyw}",\n""")

class Release():
    def __init__(self, path=".", sys="git"):
        self.path = Path(path).resolve()
        self.gh = GitHub(sys, str(self.path))
        self.pypi = PyPI_Up(str(self.path))

    def release(self, creds, pypi=True, gh=True):
        if not creds: raise ValueError("Credentials not passed")
        self.pypi.build()
        self.pypi.check()
        if gh:
            self.gh.git_add()
            self.gh.commit(creds["commit_msg"])
            self.gh.remote(creds["url"])
            self.gh.push()
        if pypi:
            self.pypi.upload(creds["pypi_token"])
        return True