from setuptools import setup, find_packages
#from importlib.metadata import version
import tomllib

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Load metadata from pyproject.toml
with open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)
project = pyproject["metadata"]

setup(
    name=project["name"],  # Replace with your package's name
    version=project["version"],  # Replace with your package's version
    author=project["authors"][0]["name"],  # Your name
    author_email=project["authors"][0]["email"],  # Your email
    description="A lightweight and extendable Python package designed to simplify interaction with Comptox APIs for toxicology analysis.",  # Brief description
    long_description=long_description,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of README.md
    url=project["homepage"],  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find all packages and subpackages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License-Expression :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=project["python_requires"],  # Specify Python version compatibility
    install_requires=[],
    include_package_data=True,  # Include files from MANIFEST.in
    project_urls={
        "Bug Tracker": project["bug_tracker"],
        "Documentation": project["documentation"],
        "Source Code": project["source_code"],
    },
)
