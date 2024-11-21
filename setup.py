from setuptools import setup, find_packages

# Read the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

about = {}
with open("pycomptox/_version.py") as f:
    exec(f.read(), about)

setup(
    name=about["__name__"],  # Replace with your package's name
    version=about["__version__"],  # Replace with your package's version
    author=about["__author__"],  # Your name
    author_email=about["__author_email__"],  # Your email
    description="A short description of your package",  # Brief description
    long_description=long_description,  # Detailed description from README.md
    long_description_content_type="text/markdown",  # Format of README.md
    url=about["__url__"],  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find all packages and subpackages
    classifiers=[
        "Programming Language :: Python :: 3",
        f"License :: {about['__license__']}",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",  # Specify Python version compatibility
    install_requires=[
        # Add dependencies here
        "requests>=2.0.0",  # Example dependency
    ],
    entry_points={
        "console_scripts": [
            # Example command-line tool
            "mypackage-cli=mypackage.module1:main_function",
        ],
    },
    include_package_data=True,  # Include files from MANIFEST.in
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/mypackage/issues",
        "Documentation": "https://github.com/yourusername/mypackage#readme",
        "Source Code": "https://github.com/yourusername/mypackage",
    },
)
