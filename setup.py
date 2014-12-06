#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import echo_seeds
version = echo_seeds.__version__

setup(
    name='echo_seeds',
    version=version,
    author='',
    author_email='briandant414@gmail.com',
    packages=[
        'echo_seeds',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.7.1',
    ],
    zip_safe=False,
    scripts=['echo_seeds/manage.py'],
)
