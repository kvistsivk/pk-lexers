from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ('BoxCodeLexer')

class BoxCodeLexer(RegexLexer):
    name = 'Box Code'
    aliases = ['box_code']
    filenames = []

    box_name = r'(Box\s+\d+:\s+)'
    box_str = r'([0-9A-F]{2})( )([0-9A-F]{2})( )([0-9A-F]{2})( )([0-9A-F]{2})'
    box_line = "{}{}".format(box_name, box_str)

    tokens = {
        'root': [
            include('whitespace'),
            (box_line,
             bygroups(Text, Keyword, Text, String, Text, Keyword, Text, String),
             'even_line'),
        ],

        'even_line': [
            include('whitespace'),
            (box_line,
             bygroups(Text, String, Text, Keyword, Text, String, Text, Keyword),
             '#pop'),
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'#.*?\n', Comment),
        ],
    }
