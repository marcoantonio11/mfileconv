import os

from setuptools import find_packages, setup


def read(*paths):
    """Read the contents of a text file safely.
    >>> read("mfileconv", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]


setup(
    name="mfileconv",
    version="0.1.0",
    description="Convert files to other formats",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Marco Silva",
    author_email="marcoa.silva84@gmail.com",
    python_requires=">=3.11",
    packages=find_packages(exclude=["integration", "tests"]),
    include_package_data=True,
    entry_points={"console_scripts": ["mfileconv = mfileconv.__main__:main"]},
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt"),
    },
)
