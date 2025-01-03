from pygments.lexer import RegexLexer, include
from pygments.token import *

__all__ = ("Gen3AceLexer")

class Gen3AceLexer(RegexLexer):
    name = 'Gen 3 ACE'
    aliases = ['gen3ace']
    filenames = ['*.asm']

    register = '(?:{})'.format('|'.join([
        'r0', 'r1(?:0|1|2|3|4|5)?', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8',
        'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'sb', 'sl', 'fp', 'ip',
        'sp', 'lr', 'pc',
    ]))

    cond = '(?:{})'.format('|'.join([
        'AL', 'CC', 'CS', 'EQ', 'GE', 'GT', 'HI', 'HS', 'LE', 'LO', 'LS', 'LT',
        'MI', 'NE', 'PL', 'VC', 'VS',
    ]))

    op_c = '(?:{}){}?'.format('|'.join([
        'B(?:L|X)?', 'CMN', 'CMP', 'LDR(?:B|H|SB|SH)?', 'POP', 'PUSH',
        'STR(?:B|H)?', 'TEQ', 'TST',
    ]), cond)

    op_sc = '(?:{})S?{}?'.format('|'.join([
        'ADC', 'ADD', 'AND', 'ASR', 'BIC', 'EOR', 'LSL', 'LSR', 'MLA', 'MOV',
        'MUL', 'MVN', 'ORR', 'ROR', 'RRX', 'RSB', 'RSC', 'SBC', 'SMLAL',
        'SMULL', 'SUB', 'UMLAL', 'UMULL',
    ]), cond)

    op_ac = '(?:LDM|STM)(?:IA|IB|DA|DB)?{}?'.format(cond)

    instruction = '(?:{})'.format('|'.join([op_c, op_sc, op_ac, 'NOP']))

    tokens = {
        'root': [
            include('whitespace'),

            (r'[0-9A-Z]{2}(?: [0-9A-Z]{2}){3}', String),
            (register, Keyword),
            (instruction, Name.Constant),
            (r'#0x[0-9A-F]+', Number.Hex),
            (r'#0b[01]+', Number.Bin),
            (r'#\d+', Number.Integer),
            (r'[-*,.():]+', Punctuation)
        ],

        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
            (r';.*?\n', Comment),
        ],

        'punctuation': [
            (r'[-*,.():!\[\]]+', Punctuation)
        ]
    }
