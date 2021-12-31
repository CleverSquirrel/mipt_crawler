# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

# def read(filename: str) -> str:
#     with open(os.path.join(os.path.dirname(__file__), filename)) as file:
#         return file.read()


# def parse_requirements() -> tuple:
#     """Parse requirements.txt for install_requires"""
#     requirements = read("requirements.txt")
#     return tuple(requirements.split("\n"))


setup(
    name="crawler",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
