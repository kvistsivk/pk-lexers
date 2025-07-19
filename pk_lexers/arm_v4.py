from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ('ArmV4Lexer')

class ArmV4Lexer(RegexLexer):
    name = 'ARMv4'
    aliases = ['arm_v4']
    filenames = []

    hex_byte = r'[0-9A-F]{2}'
    var_byte = r'[a-z]{2}'
    hh_word = r'({})( )({})'.format(hex_byte, hex_byte)
    hv_word = r'({})( )({})'.format(hex_byte, var_byte)
    vh_word = r'({})( )({})'.format(var_byte, hex_byte)
    vv_word = r'({})( )({})'.format(var_byte, var_byte)

    cond = r'CC|CS|EQ|GE|GT|HI|HS|LE|LO|LS|LT|MI|NE|NV|PL|VC|VS'

    op6 = r'SMLALS|SMULLS|UMLALS|UMULLS'
    op5 = r'LDMDA|LDMDB|LDMIA|LDMIB|LDRSB|LDRSH|SMLAL|SMULL|STMDA|STMDB|STMIA|STMIB|UMLAL|UMULL'
    op4 = (
        r'ADCS|ADDS|ANDS|ASRS|BICS|EORS|LDRB|LDRH|LSLS|LSRS|MLAS|MOVS|MULS|MVNS|ORRS|PUSH|RORS|'
        r'RRXS|RSBS|RSCS|SBCS|STRB|STRH|SUBS'
    )

    op3 = (
        r'ADC|ADD|AND|ASR|BIC|BLX|CMN|CMP|EOR|LDM|LDR|LSL|LSR|MLA|MOV|MRS|MSR|MUL|MVN|ORR|POP|ROR|'
        r'RRX|RSB|RSC|SBC|STM|STR|SUB|TEQ|TST'
    )

    op2 = r'BL|BX'
    op1 = r'B'

    op6_cond = r'(?:{})(?:{})'.format(op6, cond)
    op5_cond = r'(?:{})(?:{})'.format(op5, cond)
    op4_cond = r'(?:{})(?:{})'.format(op4, cond)
    op3_cond = r'(?:{})(?:{})'.format(op3, cond)
    op2_cond = r'(?:{})(?:{})'.format(op2, cond)
    op1_cond = r'(?:{})(?:{})'.format(op1, cond)

    op_bare = r'ADR|CPY|DCB|DCD|DCI|DCQ|DCW|NOP'
    directive = r'\.(?:ascii|byte|hword|req|word)'

    register = r'(?:{})(?![0-9A-Za-z_./])'.format('|'.join([
        '[cs]psr(?:_fs?x?c?|_sx?c?|_xc?|_c)?',
        'r1[0-5]', 'r[0-9]',
        'fp',
        'ip',
        'lr',
        'pc',
        'sb',
        'sl',
        'sp',
    ]))

    string = r'"[^"]*?"'
    bin_num = r'0b[01]+'
    oct_num = r'0o[0-7]+'
    dec_num = r'[0-9]+'
    hex_num = r'0x[0-9a-fA-F]+'
    label = r'[A-Za-z_][0-9A-Za-z_./]+'
    const = r'([#])({})'.format(label)

    tokens = {
        'root': [
            (hh_word, bygroups(Generic, Text, Generic)),
            (hv_word, bygroups(Generic, Text, Generic.Emph)),
            (vh_word, bygroups(Generic.Emph, Text, Generic)),
            (vv_word, bygroups(Generic.Emph, Text, Generic.Emph)),

            (op6_cond, Operator.Word),
            (op5_cond, Operator.Word),
            (op6, Operator.Word),
            (op4_cond, Operator.Word),
            (op5, Operator.Word),
            (op3_cond, Operator.Word),
            (op4, Operator.Word),
            (op2_cond, Operator.Word),
            (op3, Operator.Word),
            (op1_cond, Operator.Word),
            (op2, Operator.Word),
            (op1, Operator.Word),
            (op_bare, Operator.Word),
            (directive, Operator.Word),

            (register, Name.Variable.Global),
            (string, String),
            (bin_num, Number.Bin),
            (oct_num, Number.Oct),
            (hex_num, Number.Hex),
            (dec_num, Number.Integer),
            (const, bygroups(Punctuation, Number.Integer)),
            (label, Name.Label),

            (r'\n', Text),
            (r'\s+', Text),
            (r'@.*?\n', Comment),
            (r'[-*.,(){}:;\[\]!]+', Punctuation),
        ],
    }

