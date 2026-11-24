from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="Sadr",
    version="0.5.3",
    description="A Python package publishing framework",

    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",

    packages=find_packages(),
    python_requires=">=3.8",

    install_requires=[
        "requests>=2.31.0"
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Build Tools",
    ],

    keywords="pypi python publishing package",
)
