from pathlib import Path
import subprocess as sp
import sys
import requests
import shutil

class PyPI_Up:
    def __init__(self, pr_dir="."):
        self.pr_dir = Path(pr_dir).resolve()
        self.dist_dir = self.pr_dir / "dist"

    def _run(self, *cmd):
        return sp.run(
            [sys.executable, *cmd],
            cwd=self.pr_dir,
            check=True
        )

    def val(self):
        required = ["pyproject.toml", "README.md"]
        missing = [
            file for file in required
            if not (self.pr_dir / file).is_file()
        ]
        if missing:
            raise FileNotFoundError(
                f"Missing project files: {', '.join(missing)}"
            )
        return True

    def build(self, clean=False):
        self.val()
        if clean and self.dist_dir.exists():
            for file in self.dist_dir.iterdir():
                if file.is_file(): file.unlink()
        self._run("-m", "build")
        return list(self.dist_dir.glob("*"))

    def inspect(self):
        if not self.dist_dir.exists(): raise FileNotFoundError("Distribution directory not found")
        files = list(self.dist_dir.glob("*"))
        if not files: raise FileNotFoundError("No distributions found")
        return [
            {
                "name": file.name,
                "size": file.stat().st_size,
                "type": file.suffix
            }
            for file in files
            if file.is_file()
        ]

    def check_twine(self):
        try:
            self._run("-m", "twine", "--version")
            return True
        except sp.CalledProcessError: return False

    def check(self):
        if not self.check_twine(): raise RuntimeError("Twine is not installed")
        self._run(
            "-m", "twine",
            "check",
            "dist/*"
        )
        return True

    def upload(self, token, repository="pypi"):
        if not token: raise ValueError("PyPI API token cannot be empty")
        if not self.dist_dir.exists(): raise FileNotFoundError("Build the project first")
        distributions = [
            str(file)
            for file in self.dist_dir.glob("*")
            if file.is_file()
        ]
        if not distributions: raise FileNotFoundError("No distributions to upload")
        self._run(
            "-m", "twine",
            "upload",
            "--repository", repository,
            "--username", "__token__",
            "--password", token,
            *distributions
        )
        return True

class PyPI_Manage:
    def __init__(self, dir="."):
        self.path = Path(dir).resolve()

    def _run(self, *cmd):
        return sp.run(
            [*cmd],
            cwd=self.path,
            check=True
        )

    def install(self, name):
        self._run("pip", "install", name)

    def get_package(self, name):
        url = f"https://pypi.org/pypi/{name}/json"
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None

    def get_versions(self, name):
        package = self.get_package(name)
        if not package: return []
        url = f"https://pypi.org/pypi/{name}/json"
        r = requests.get(url)
        if r.status_code != 200: return []
        return list(r.json()["releases"].keys())

    def get_latest(self, name):
        package = self.get_package(name)
        if not package: return None
        return package["info"]["version"]

    def get_release(self, name, version):
        url = f"https://pypi.org/pypi/{name}/{version}/json"
        r = requests.get(url)
        return r.json() if r.status_code == 200 else None

    def delete_local(self):
        build = self.path / "build"
        dist = self.path / "dist"
        egg = self.path / "*.egg-info"
        if build.exists(): shutil.rmtree(build)
        if dist.exists(): shutil.rmtree(dist)
        for folder in self.path.glob("*.egg-info"): shutil.rmtree(folder)
        return True

    def check_name(self, name):
        url = f"https://pypi.org/pypi/{name}/json"
        r = requests.get(url)
        return r.status_code == 404

    def get_downloads(self, name, period="month"):
        url = (
            f"https://pypistats.org/api/packages/"
            f"{name}/recent"
        )
        r = requests.get(url, params={"period": period})
        if r.status_code != 200: return None
        return r.json()
