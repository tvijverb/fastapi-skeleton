#!/usr/bin/env python3

from setuptools import setup, find_namespace_packages

exclude = []

setup(
    name='fastapi-skeleton',
    # version='1.0',
    description='Skeleton REST API',
    author='Thomas Vijverberg',
    author_email='thomas@vijverb.nl',
    packages=find_namespace_packages(exclude=exclude),
    include_package_data=True,
)
