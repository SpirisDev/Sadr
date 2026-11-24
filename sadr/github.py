from pathlib import Path
import subprocess as sp

class GitHub:
    def __init__(self, git, path="."):
        self.path = Path(path).resolve()
        self.git = git

    def _run(self, *cmd):
        return sp.run(
            [self.git, *cmd],
            cwd=self.path,
            check=True
        )

    def check_git(self):
        try:
            self._run("--version")
            return True
        except:
            return False

    def git_init(self):
        self._run("init")

    def git_add(self):
        self._run("add", ".")

    def commit(self, msg):
        self._run("commit", "-m", msg)

    def remote(self, url):
        self._run("remote", "add", "origin", url)

    def push(self):
        self._run("branch", "-M", "main")
        self._run("push", "-u", "origin", "main")

    def upload(self, url, msg="You Forgot the message for commit :)"):
        self.git_init()
        self.git_add()
        self.commit(msg)
        self.remote(url)
        self.push()

    def pull(self, remote="origin", branch="main", rebase=True):
        if rebase: self._run("pull", "--rebase", remote, branch)
        else: self._run("pull", remote, branch)

    def log(self, count=10):
        return self._run(
            "log", f"-{count}",
            "--oneline",
            capture_output=True
        ).stdout

    def create_branch(self, name):
        self._run("branch", name)
        return True

    def switch(self, name):
        self._run("switch", name)
        return True

    def delete_branch(self, name):
        self._run("branch", "-d", name)
        return True

    def clone(self, url, path=None):
        target = Path(path).resolve() if path else self.path
        sp.run(
            [self.git, "clone", url, str(target)],
            check=True,
            text=True
        )
        self.path = target
        return True
