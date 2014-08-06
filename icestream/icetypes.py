_types = {}


class TypeMeta(type):
    def __new__(cls, name, bases, dct):
        #print "[ __new__ ] ========================================="
        #print "    cls      : ", cls
        #print "    name     : ", name
        #print "    bases    : ", bases
        #print "    dct      : ", dct
        #print " ---------------------------------------------------- "
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        #print "[ __init__ ] ========================================="
        #print "    cls      : ", cls
        #print "    name     : ", name
        #print "    bases    : ", bases
        #print "    dct      : ", dct
        #print " ---------------------------------------------------- "

        cls.register_type(bases[0])
        super(TypeMeta, cls).__init__(name, bases, dct)

    def register_type(cls, base):
        try:
            cls_name = base.type_name(cls)
            global _types
            _types[cls_name] = cls
        except:
            pass


class BuildinType(object):
    __metaclass__ = TypeMeta

    @staticmethod
    def type_name(cls):
        if cls == BuildinType:
            return None
        return cls.__name__.lower()


class Bool(BuildinType):
    def __init__(self):
        print "bool __init__"

class Byte(BuildinType):
    pass


class Short(BuildinType):
    pass


class Int(BuildinType):
    pass


class Long(BuildinType):
    pass


class Float(BuildinType):
    pass


class Double(BuildinType):
    pass


class String(BuildinType):
    pass


class IceModule:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
    
    def __repr__(self):
        return "Module<%s>" % self.name


class VarType:
    def __init__(self, name, domain=None):
        self.name = name
        self.domain = domain

    def var_name(self):
        path = (self.domain or []) + [self.name]
        return ".".join(path)


class Member:
    def __init__(self, var_type, name):
        self.var_type = var_type
        self.name = name


class TypeDefine:
    def __init__(self, var_type, type_name):
        self.var_type = var_type
        self.type_name = type_name


class Content(object):
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name


class ConstData(Content):
    def __init__(self, name, var_type, data):
        super(ConstData, self).__init__(name)
        self.var_type = var_type
        self.data = data


class Struct(Content):
    def __init__(self, name, members=None):
        super(Struct, self).__init__(name)
        self.members = members


class Enum(Content):
    def __init__(self, name, members=None):
        super(Enum, self).__init__(name)
        self.members = members

class EnumMember(Content):
    def __init__(self, name, val=None):
        super(EnumMember, self).__init__(name)
        self.val = val

class Interface(Content):
    def __init__(self, name, member_funcs):
        super(Interface, self).__init__(name)
        self.member_funcs = member_funcs


class MemberFunc(Content):
    def __init__(self, name, ret_type, params=None):
        super(MemberFunc, self).__init__(name)
        self.params = params
        self.ret_type = ret_type


class Param(Content):
    def __init__(self, name, var_type, out_flag=False):
        super(Param, self).__init__(name)
        self.var_type = var_type
        self.out_flag = out_flag


class Sequence(Content):
    def __init__(self, item_type_name):
        super(Sequence, self).__init__(item_type_name)
        self.item_type_name = item_type_name


class Dictionary(Content):
    def __init__(self, key, val):
        super(Dictionary, self).__init__(self.get_name(key, val))
        self.key = key
        self.val = val
        print self.name

    def get_name(self, key, val):
        return "dictionary<%s,%s>" % (key.var_name(), val.var_name())


def get_type(name):
    global _types
    try:
        return _types[name]
    except:
        raise Exception("unknown type: %s" % name)


def get_sequence_type(item_name):
    cls_name = "sequence<%s>" % (item_name)

    try:
        return get_type(cls_name)
    except:
        pass

    item_type = get_type(item_name)

