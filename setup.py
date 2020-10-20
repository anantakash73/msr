from setuptools import setup, find_packages
from io import open
from os import path
import pathlib
HERE = pathlib.Path(__file__).parent

with open("README.md", "r") as fh:
    long_description = fh.read()
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
                    if 'git+' not in x]

setup(
    name="msr-anant", # Replace with your own username
    version="0.0.1",
    author="Anant Akash",
    author_email="anant@example.com",
    description="A small package to check page load times",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anantakash73/msr",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)