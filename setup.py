# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open("README.md") as f:
    readme = f.read()


setup(
    name="sphinxdemo",
    description="Sample package for documentation with Sphinx.",
    long_description=readme,
    author="Andy Disch",
    author_email="andy.disch@eawag.ch",
    packages=find_packages(exclude=("test", "doc")),
)
