#!/usr/bin/env python3
from distutils.core import setup
import os

if os.path.exists('README.rst'):
    long_description = open('README.rst', encoding = 'UTF-8').read()
else:
    long_description = 'See http://github.com/jwandborg/py-colorclassifier'

setup(
    name = 'colorclassifier',
    version = '2.0.0',
    description = 'Color classifier',
    long_description = long_description,
    author = 'Joar Wandborg',
    author_email = 'python@wandborg.se',
    url = 'https://github.com/jwandborg/py-colorclassifier',
    packages = ['colorclassifier'],
    requires = ['colormath'],
    classifiers = [
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.0',
        'Topic :: Utilities',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ]
    )
