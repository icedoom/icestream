from .context import *
from .icetypes import *


class Module:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members or []

    @stack_ctx
    def build(self, ctx):
        print "now to handle module <%s>" % self.name
        ctx.build_items(self.members)

    def __repr__(self):
        return "Module<%s>" % self.name

    def con_type(self):
        return IceModule(self.name)

    def ice_mod_name(self):
        return self.name


class VarType:
    def __init__(self, name, domain=None):
        self.name = name
        self.domain = domain
        self.path = (self.domain or []) + [self.name]

    def var_name(self):
        return ".".join(self.path)

    def cls_name(self):
        return "_".join(self.path)

    def __repr__(self):
        return "_".join(self.path)

    def get_type(self, ctx):
        type_name = self.var_name()

        try:
            return get_buildin_type(type_name)
        except:
            pass

        member = ctx.get_member(self.path)
        if isinstance(member, CustomType) or issubclass(member, (dict, list)):
            return member
        else:
            raise TypeError("%s is not a type" % type_name)


def get_var_value(ctx, data):
    if isinstance(data, VarType):
        data = ctx.get_member(data.path)
    try:
        return data.val
    except:
        return data


class Item(object):
    def __init__(self, name):
        self.name = name

    def exist(self, ctx):
        try:
            member = ctx[self.name]
            return True
        except:
            return False

    def build(self, ctx):
        print "now to build %s" % self
        if self.exist(ctx):
            raise AttributeError("%s already exists in %s" % (self.name, ctx.cur_name()))

        self._add_item(ctx)

    def _build(self, ctx):
        raise NotImplementError(self.name)

    def _add_item(self, ctx):
        mod = self._build(ctx)
        ctx[self._item_name()] = mod
        return mod

    def _item_name(self):
        return self.name

    def __repr__(self):
        return "%s :%s" % (self.name, self.__class__)


class Member(Item):
    def __init__(self, name, var_type):
        super(Member, self).__init__(name)
        self.var_type = var_type

    def _build(self, ctx):
        return self.var_type.get_type(ctx)

    def _item_name(self):
        return "_type_%s" % self.name


class CustomType(Item):
    def __init__(self, name):
        super(CustomType, self).__init__(name)


class MemberConType(CustomType):
    class DataContainer:
        def __init__(self):
            pass

    def __init__(self, name, members=None):
        super(MemberConType, self).__init__(name)
        self.members = members or []

    def _before_build_member(self, member, ctx):
        pass

    def _after_build_member(self, member, ctx):
        pass

    def _before_build_members(self, ctx):
        pass

    def _after_build_members(self, ctx):
        pass

    @stack_ctx
    def _build(self, ctx):
        self._before_build_members(ctx)

        for member in self.members:
            self._build_member(member, ctx)

        self._after_build_members(ctx)
        attr = ctx.mod().__dict__

        return type(self.name, (self.impl_cls(),), attr)

    def impl_cls(self):
        raise NotImplementError("not implement ")

    def _build_member(self, member, ctx):
        self._before_build_member(member, ctx)
        member.build(ctx)
        self._after_build_member(member, ctx)

    def con_type(self):
        return MemberConType.DataContainer()

    def ice_mod_name(self):
        return self.name


class TypeDefine(CustomType):
    def __init__(self, var_type, name):
        super(TypeDefine, self).__init__(name)
        self.var_type = var_type

    def _build(self, ctx):
        return self.var_type.to_class(ctx)


class ConstData(Item):
    def __init__(self, name, var_type, data):
        print "const data", name, var_type, data
        super(ConstData, self).__init__(name)
        self.var_type = var_type
        self.data = data

    def _build(self, ctx):
        var_type = self.var_type.get_type(ctx)
        data = get_var_value(ctx, self.data)
        return var_type(data)


class Struct(MemberConType):

    def __init__(self, name, members=None):
        super(Struct, self).__init__(name, members)
        self._member_names = []

    def _after_build_member(self, member, ctx):
        ctx[member.name] = None
        self._member_names.append(member.name)

    def _after_build_members(self, ctx):
        ctx["_member_names"] = self._member_names

    def impl_cls(self):
        return IceStruct


class Enum(MemberConType):
    def __init__(self, name, members=None):
        super(Enum, self).__init__(name, members)

    def impl_cls(self):
        return IceEnum


class EnumMember(CustomType):
    def __init__(self, name, val=None):
        super(EnumMember, self).__init__(name)
        self.val = val

    def _build(self, ctx):
        return self.get_value(ctx)

    def get_value(self, ctx):
        val = get_var_value(ctx, self.val)
        if isinstance(val, (Int, int)):
            return val
        raise SyntaxError("invalid type")

    def __str__(self):
        return "%s = %s" % (self.name, self.val)


class Interface(MemberConType):
    def __init__(self, name, members=None):
        super(Interface, self).__init__(name, members)

    def impl_cls(self):
        return IceInterface

    def ice_mod_name(self):
        return "%sPrx" % self.name


class MemberFunc(MemberConType):
    def __init__(self, name, ret_type, in_params=None, out_params=None):
        members = (in_params or []) + (out_params or [])
        super(MemberFunc, self).__init__(name, members)
        self.ret_type = ret_type

        self.in_param_list = []
        self.out_param_list = []

    def _before_build_members(self, ctx):
        ctx["_ice_in_params"] = []
        ctx["_ice_out_params"] = []

    def _after_build_member(self, member, ctx):
        if member.is_out():
            self.out_param_list.append(member.name)
        else:
            self.in_param_list.append(member.name)
            ctx[member.name] = None

    def _after_build_members(self, ctx):
        ctx["_ice_in_params"] = self.in_param_list
        ctx["_ice_out_params"] = self.out_param_list
        ctx["_type__return_"] = self.ret_type.get_type(ctx)

    def impl_cls(self):
        return IceInterfaceFunction


class Param(Member):
    def __init__(self, name, var_type, out_flag=False):
        super(Param, self).__init__(name, var_type)
        self.out_flag = out_flag

    def is_out(self):
        return self.out_flag


class Container(CustomType):
    _c_types = {}

    def __init__(self, *item_types):
        names = [self.__class__.__name__] + [str(item) for item in item_types]
        super(Container, self).__init__("__".join(names))

        self.item_types = item_types

    def get_type(self):
        return Container._c_types[self.name]

    def set_type(self, new_type):
        Container._c_types[self.name] = new_type
        return new_type

    def __getitem__(self, idx):
        return self.item_types[idx]

    def to_class(self, ctx):
        try:
            return self.get_type()
        except:
            return self.set_type(self.gen_cls(ctx))

    def gen_cls(self, ctx):
        raise NotImplementError(self.name)


class Sequence(Container):
    def __init__(self, item_type):
        super(Sequence, self).__init__(item_type)

    def gen_cls(self, ctx):
        item_type = self[0].get_type(ctx)
        return type(self.name, (IceSequence, ), {'_val_type': item_type})


class Dictionary(Container):
    def __init__(self, key_type, val_type):
        super(Dictionary, self).__init__(key_type, val_type)

    def gen_cls(self, ctx):
        dct = {
            "_key_type": self[0].get_type(ctx),
            "_val_type": self[1].get_type(ctx)
        }

        return type(self.name, (IceDictionary,), dct)

