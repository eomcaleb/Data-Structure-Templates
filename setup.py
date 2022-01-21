import os
from setuptools import setup

setup (
    name="data-structure-template",
    version="0.0.1",
    description="Common Data Structures",
    long_description=open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
    ).read(),
    long_description_content_type="text/markdown",
    author="Caleb Eom",
    packages=["data-structure-tempalte"],
    install_requires=["setuptools", "docopt"]
)