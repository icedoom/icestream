import ply.yacc as yacc

from .icelex import tokens
from .icelex import IceLexer
from .component import *


def build_statement(p, has_comma=False):
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[(2, 3)[has_comma]]]


def build_object(obj_type, p):
    print obj_type, (p)
    if len(p) == 7:
        p[0] = obj_type(p[2], p[4])
    else:
        p[0] = obj_type(p[2])


def p_ice_file(p):
    """ice_file : MACRO_IFNDEF ID MACRO_DEFINE ID file_statement MACRO_ENDIF"""

    if p[2] != p[4]:
        raise Exception("no match id(%s) in ifndef - define" % p[2])

    p[0] = p[5]


def p_file_statement(p):
    """file_statement   :
                        | modules
                        | include_modules
                        | include_modules modules """

    if len(p) == 3:
        p[0] = p[1] + p[2]
    elif len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = []


def p_include_modules(p):
    """include_modules  : include_module
                        | include_modules include_module"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_include_module(p):
    """include_module : MACRO_INCLUDE ICE_FILE"""
    p[0] = parse(p[2][1], p.parser._ice_file_locator)


def p_modules(p):
    """modules  : module
                | modules module"""
    build_statement(p)


def p_module(p):
    """module   : MODULE ID '{' module_members '}' END
                | MODULE ID '{' '}' END """
    if len(p) == 7:
        p[0] = Module(p[2], p[4])
    else:
        p[0] = Module(p[2])

    print "got module <%s>" % p[2]


def p_module_members(p):
    """module_members   : module_member
                        | module_members module_member"""
    build_statement(p)


def p_module_member(p):
    """module_member    : module
                        | type_define
                        | struct
                        | interface
                        | const_data
                        | enum """
    p[0] = p[1]


def p_const_data(p):
    """const_data   : CONST var_type ID '=' data END """
    p[0] = ConstData(p[3], p[2], p[5])


def p_data(p):
    """data : NUMBER
            | BOOL
            | FLOAT
            | STRING """
    p[0] = p[1]


def p_data_var(p):
    """data : var_type"""
    p[0] = p[1]


def p_type_define(p):
    """type_define  : sequence_type ID END
                    | dictionary_type ID END """
    p[0] = TypeDefine(p[1], p[2])


def p_enum(p):
    """enum : ENUM ID '{' enum_members '}' END """
    p[0] = Enum(p[2], p[4])


def p_enum_members(p):
    """enum_members : enum_member
                    | enum_members enum_member"""
    build_statement(p)


def p_enum_member(p):
    """enum_member  : ID ','
                    | ID '=' NUMBER ','
                    | ID '=' var_type ',' """
    if len(p) == 3:
        p[0] = EnumMember(p[1])
    else:
        p[0] = EnumMember(p[1], p[3])


def p_sequence_type(p):
    """sequence_type : SEQUENCE '<' var_type '>' """
    p[0] = Sequence(p[3])


def p_dictionary_type(p):
    """dictionary_type  : DICTIONARY '<' var_type ',' var_type '>' """
    p[0] = Dictionary(p[3], p[5])


def p_var_type(p):
    """var_type : ID
                | domain ID """
    if len(p) == 2:
        p[0] = VarType(p[1])
    else:
        p[0] = VarType(p[2], p[1])


def p_domain(p):
    """domain   : DOMAIN
                | ID DOMAIN
                | domain ID DOMAIN """

    if len(p) == 2:
        p[0] = ['.']
    elif len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


def p_struct(p):
    """struct   : STRUCT ID '{' data_members '}' END """
    build_object(Struct, p)


def p_data_members(p):
    """data_members : data_member
                    | data_members data_member"""
    build_statement(p)


def p_data_member(p):
    """data_member  : var_type ID END"""
    p[0] = Member(p[2], p[1])


def p_interface(p):
    """interface    : INTERFACE ID '{' member_funcs '}' END
                    | INTERFACE ID '{' '}' END """
    build_object(Interface, p)


def p_member_funcs(p):
    """member_funcs : member_func
                    | member_funcs member_func"""
    build_statement(p)


def p_member_func(p):
    """member_func  : INTERFACE_TYPE var_type ID '(' params ')' END
                    | var_type ID '(' params ')' END
                    | var_type ID '(' ')' END """
    if len(p) == 8:
        p[0] = MemberFunc(p[3], p[2], p[5][0], p[5][1])
    elif len(p) == 7:
        p[0] = MemberFunc(p[2], p[1], p[4][0], p[4][1])
    else:
        p[0] = MemberFunc(p[2], p[1])


def p_all_in_params(p):
    """params   : in_params"""
    p[0] = p[1], []


def p_all_out_params(p):
    """params   : out_params"""
    p[0] = [], p[1]


def p_mix_params(p):
    """params   : in_params ',' out_params"""
    p[0] = p[1], p[3]


def p_in_param(p):
    """in_param : var_type ID"""
    p[0] = Param(p[2], p[1])


def p_out_param(p):
    """out_param : OUT var_type ID"""
    p[0] = Param(p[3], p[2], True)


def p_in_params(p):
    """in_params    : in_param
                    | in_params ',' in_param"""
    build_statement(p, True)


def p_out_params(p):
    """out_params   : out_param
                    | out_params ',' out_param"""
    build_statement(p, True)


def p_error(p):
    s = [p.value]
    while 1:
        tok = yacc.token()
        if not tok or tok.type == 'END':
            break
        s.append(str(tok.value))
        print s

    raise SyntaxError(" ".join(s))


def parse(file_name, file_locator):
    print "parse %s" % file_name
    parser = yacc.yacc()
    parser._ice_file_locator = file_locator
    lx = IceLexer()
    return parser.parse(file_locator.read(file_name), lexer=lx)
