import types

_types = {}

get_buildin_type = lambda n: _types[n]


class NotImplementError(Exception):
    def __init__(self, *args):
        Exception.__init__(self, *args)


def add_buildin_type(name, cls):
    _types[name] = cls


class TypeMeta(type):
    def __new__(mcs, name, bases, dct):
        return type.__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        cls.register_type(bases[0])
        super(TypeMeta, cls).__init__(name, bases, dct)

    def register_type(cls, base):
        try:
            add_buildin_type(base.type_name(cls), cls)
        except:
            pass


def get_val(name, mod, ctx):
    try:
        return getattr(mod, name)
    except:
        return ctx.get_val(name)


class BuildinType(object):
    __metaclass__ = TypeMeta

    @staticmethod
    def type_name(cls):
        if cls == BuildinType:
            return None
        return cls.__name__.lower()

    def __init__(self, val):
        self.val = val


class Bool(BuildinType):
    def __init__(self, val):
        BuildinType.__init__(self, bool(val))


class Byte(BuildinType):
    pass


class Short(BuildinType):
    def __init__(self, val):
        BuildinType.__init__(self, int(val))


class Int(Short):
    pass


class Long(Int):
    pass


class Float(BuildinType):
    pass


class Double(BuildinType):
    pass


class String(BuildinType):
    pass


class Void(BuildinType):
    pass


class IceModule(types.ModuleType):
    pass


class IceStruct(object):
    pass


class IceEnum(object):
    pass


class IceInterface(object):
    pass


class IceInterfaceFunction(object):
    pass


class IceDictionary(dict):
    pass


class IceSequence(list):
    pass

