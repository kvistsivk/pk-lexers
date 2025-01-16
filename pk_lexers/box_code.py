from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ('BoxCodeLexer')

class BoxCodeLexer(RegexLexer):
    name = 'Box Code'
    aliases = ['box_code']
    filenames = []

    box = r'(Box\s+\d+:\s+)([0-9A-F]{2}(?: [0-9A-F]{2}){3})'

    tokens = {
        'root': [
            include('whitespace'),
            (box, bygroups(Generic.Strong, String), "even-line"),
        ],

        'even-line': [
            include('whitespace'),
            (box, bygroups(Generic.Strong, String.Other), '#pop'),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r';.*?\n', Comment),
        ],
    }
