from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ('ArmV4Lexer')

class ArmV4Lexer(RegexLexer):
    name = 'ARMv4'
    aliases = ['arm_v4']
    filenames = []

    register = "(?:{})".format('|'.join([
        '[cs]psr(?:_f?s?x?c?)?', 'r0', 'r1(?:0|1|2|3|4|5)?', 'r2', 'r3', 'r4',
        'r5', 'r6', 'r7', 'r8', 'r9', 'sb', 'sl', 'fp', 'ip', 'sp', 'lr', 'pc',
    ]))

    cond = "(?:{})".format('|'.join([
        'AL', 'CC', 'CS', 'EQ', 'GE', 'GT', 'HI', 'HS', 'LE', 'LO', 'LS', 'LT',
        'MI', 'NE', 'NV', 'PL', 'VC', 'VS',
    ]))

    op_c = "(?:{}){}?".format('|'.join([
        'B(?:L|X)?', 'CMN', 'CMP', 'LDR(?:B|H|SB|SH)?', 'MRS', 'MSR', 'POP',
        'PUSH', 'STR(?:B|H)?', 'TEQ', 'TST',
    ]), cond)

    op_sc = "(?:{})S?{}?".format('|'.join([
        'ADC', 'ADD', 'AND', 'ASR', 'BIC', 'EOR', 'LSL', 'LSR', 'MLA', 'MOV',
        'MUL', 'MVN', 'ORR', 'ROR', 'RRX', 'RSB', 'RSC', 'SBC', 'SMLAL',
        'SMULL', 'SUB', 'UMLAL', 'UMULL',
    ]), cond)

    op_ac = "(?:LDM|STM)(?:IA|IB|DA|DB)?{}?".format(cond)

    instruction = "(?:{})".format('|'.join([
        op_c,
        op_sc,
        op_ac,
        'ADR',
        'CPY',
        'NOP',
        'DCB',
        'DCW',
        'DCD',
        'DCQ',
        'DCI',
    ]))

    string = r'"[^"]*?"'

    hex_byte = '[0-9A-F]{2}'
    var_byte = '[a-z]{2}'
    hh_word = '({})( )({})'.format(hex_byte, hex_byte)
    hv_word = '({})( )({})'.format(hex_byte, var_byte)
    vh_word = '({})( )({})'.format(var_byte, hex_byte)
    vv_word = '({})( )({})'.format(var_byte, var_byte)

    tokens = {
        'root': [
            (r'\n', Text),
            (r'\s+', Text),
            (r'@.*?\n', Comment),
            (r'[-*.,(){}:;\[\]!]+', Punctuation),

            (hh_word, bygroups(Generic, Text, Generic)),
            (hv_word, bygroups(Generic, Text, Generic.Emph)),
            (vh_word, bygroups(Generic.Emph, Text, Generic)),
            (vv_word, bygroups(Generic.Emph, Text, Generic.Emph)),

            (instruction, Operator.Word),
            (register, Name.Variable.Global),
            (string, String),
            (r'0x[0-9A-F]+', Number.Hex),
            (r'0b[01]+', Number.Bin),
            (r'-?\d+', Number.Integer),
            (r'[a-z_][0-9A-Za-z_.]+', Name.Label),
        ],
    }
