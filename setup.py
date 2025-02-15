#!/usr/bin/env python
"""Setup pk-lexers"""
from setuptools import setup, find_packages

entry_points = '''
[pygments.lexers]
arm_v4=pk_lexers:ArmV4Lexer
box_code=pk_lexers:BoxCodeLexer
'''

setup(
    name='pk-lexers',
    version='0.1.11',
    author='Kvist',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.0.1',
    ],
)
