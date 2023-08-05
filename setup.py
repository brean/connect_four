#!/usr/bin/env python3

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="connect_four",
    description="Four connect logic to use in any other project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brean/connect_four",
    version="1.0.0",
    license="Apache 2.0",
    author="Andreas Bresser",
    packages=find_packages(),
    tests_require=[],
    include_package_data=True,
    install_requires=[],
)
