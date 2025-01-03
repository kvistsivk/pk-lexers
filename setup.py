#!/usr/bin/env python
"""Setup pk-lexers"""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
gen3ace=pk_lexers:Gen3AceLexer
'''

setup(
    name='pk-lexers',
    version='0.1.0',
    author='Kvist',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1',
    ],
)
