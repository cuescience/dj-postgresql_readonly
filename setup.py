#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
        name='dj-postgresql_readonly',
        version='1.0',
        description='Readonly postgres django db backend. Use it if you don't have read access to a database',
        maintainer='cuescience',
        maintainer_email='kontakt@cuescience.de',
        license="MIT",
        url='',
        packages=['postgresql_readonly'],
        install_requires=[
	       "Django",
	]
     )
