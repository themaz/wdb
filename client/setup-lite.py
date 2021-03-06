#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wdb lite
"""
import os
import sys
import re
from setuptools import setup

ROOT = os.path.dirname(__file__)
with open(os.path.join(ROOT, 'wdb', '__init__.py')) as fd:
    __version__ = re.search("__version__ = '([^']+)'", fd.read()).group(1)

requires = []

if sys.version_info[:2] <= (2, 6):
    requires.append('argparse')

options = dict(
    name="wdb-lite",
    version=__version__,
    description="An improbable web debugger through WebSockets "
    "(client only, minimal dependencies)",
    long_description="See http://github.com/Kozea/wdb",
    author="Florian Mounier @ kozea",
    author_email="florian.mounier@kozea.fr",
    url="http://github.com/Kozea/wdb",
    license="GPLv3",
    platforms="Any",
    packages=['wdb'],
    provides=['wdb'],
    install_requires=requires,
    entry_points={'console_scripts': [
        'wdb=wdb.__main__:main',
        'wdb-%s=wdb.__main__:main' % sys.version[:3]]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Debuggers"])

setup(**options)
