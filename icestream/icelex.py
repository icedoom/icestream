import ply.lex as lex
from ply.lex import TOKEN

tokens = [
    'NUMBER',
    'ID',
    'ICE_FILE',
    'STRING',
    'BOOL',
    'FLOAT',
    'INTERFACE_TYPE',
    'MACRO_IFNDEF',
    'MACRO_DEFINE',
    'MACRO_INCLUDE',
    'MACRO_ENDIF',
    'END',
    'DOMAIN',
    'COMMENT',
]

reserved = {
    'module'    : 'MODULE',
    'struct'    : 'STRUCT',
    'interface' : 'INTERFACE',
    'out'       : 'OUT',
    'sequence'  : 'SEQUENCE',
    'dictionary': 'DICTIONARY',
    'const'     : 'CONST',
    'enum'      : "ENUM",
}

tokens = tokens + list(reserved.values())


def IceLexer():

    literals = '''<>[]{},()='''

    t_ignore = ' \t'


    t_END = ';+'
    t_DOMAIN = '::'

    dir_re = r'[a-zA-Z0-9_]+'
    ice_file_re = "%s(/%s)*\.ice" % (dir_re, dir_re)
    id_re = r'[a-zA-Z_][a-zA-Z0-9_]*'

    t_MACRO_IFNDEF = '\#ifndef'
    t_MACRO_DEFINE = '\#define'
    t_MACRO_ENDIF  = '\#endif'
    t_MACRO_INCLUDE= '\#include'

    def t_COMMENT(t):
        r"""(/\*(.|\n)*\*/)|(//.*)"""
        pass

    def t_BOOL(t):
        r'(true|false)'
        t.value = (False, True)[t.value == 'true']
        return t

    def t_FLOAT(t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INTERFACE_TYPE(t):
        r'\["(amd|ami)"\]'
        t.value = t.lexer.lexmatch.groups()[1]
        return t

    @TOKEN('''(<%s>|"%s")''' % (ice_file_re, ice_file_re))
    def t_ICE_FILE(t):
        file_name = t.value[1:-1]
        file_type = ('sys', 'usr')[t.value[0] == '"']
        t.value = (file_type, file_name)
        return t

    def t_STRING(t):
        r'"(\\"|[^"]*)"'
        t.value = t.value[1:-1]
        return t

    def t_NUMBER(t):
        r"""([+-]?)(0x[A-Fa-f0-9]+|\d+)"""

        num = t.value
        sign = 1
        if num[0] in '+-':
            if num[0] == '-':
                sign = -1
            num = num[1:]

        if num.startswith('0x'):
            num = int(num, 16)
        else:
            num = int(num)
        t.value = sign * num
        return t

    @TOKEN(id_re)
    def t_ID(t):
        t.type = reserved.get(t.value, 'ID')
        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)

    lx = lex.lex()
    return lx
