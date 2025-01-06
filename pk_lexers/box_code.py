from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ('BoxCodeLexer')

class BoxCodeLexer(RegexLexer):
    name = 'Box Code'
    aliases = ['box_code']
    filenames = []

    box_name = r'(Box\s+\d+:\s+)([0-9A-F]{2}(?: [0-9A-F]{2}){3})'
    box_str = r'([0-9A-F]{2})( )([0-9A-F]{2})( )([0-9A-F]{2})( )([0-9A-F]{2})'
    box_line = "{}{}".format(box_name, box_str)

    tokens = {
        'root': [
            include('whitespace'),
            (box_name, bygroups(Name, Keyword), "even_line"),
        ],

        'even_line': [
            include('whitespace'),
            (box_name, bygroups(Name, String), '#pop'),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r';.*?\n', Comment),
        ],
    }
