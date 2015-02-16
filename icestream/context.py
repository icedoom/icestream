import types
from functools import wraps


class Info:
    def __init__(self, name, val):
        self._add_member("_name", name)
        self._add_member("_val", val)

    def __setattr__(self, key, value):
        return setattr(self._val, key, value)

    def __getattr__(self, item):
        return getattr(self._val, item)

    def __str__(self):
        return self._name

    def __repr__(self):
        return "<%s:%s>" % (repr(self._val), self._name)

    def _add_member(self, key, val):
        self.__dict__[key] = val

    def get_mod(self):
        return self._val


class MemberNotExist(AttributeError):
    def __init__(self, member_name):
        super(MemberNotExist, self).__init__("%s not exists" % member_name)


class Context:
    def __init__(self, name):
        self.cur = None
        name += "_ctx"
        self.__path = [Info(name, types.ModuleType(name))]

        self._set_cur()

    def update(self, mod):
        print "now start to build Module<%s>" % mod.name
        mod.build(self)

    def __setitem__(self, key, value):
        setattr(self.cur, key, value)

    def __getitem__(self, item):
        return getattr(self.cur, item)

    def push(self, item):
        con = item.con_type()
        setattr(self.cur, item.name, con)

        info = Info(item.name, con)

        self.__path.append(info)

        old, cur = self._set_cur()

        self.set_ice_mod(item.ice_mod_name())

        return cur

    def pop(self):
        del self.__path[-1]

        old, cur = self._set_cur()
        return old

    def _set_cur(self):
        old = self.cur

        try:
            self.cur = self.__path[-1]
        except:
            self.cur = None

        return old, self.cur

    def path(self):
        return [info.name for info in self.__path][1:]

    def build_items(self, items):
        for item in items:
            item.build(self)

    def get_member(self, names):
        if type(names) is str:
            names = names.split('::')

        cur = None
        for n in names:
            cur = self.get_ctx(n, cur)
        return cur

    def get_ctx(self, name, cur=None):
        if cur is not None:
            return getattr(cur, name)

        for node in reversed(self.__path):
            try:
                return getattr(node, name)
            except:
                pass

        raise MemberNotExist("%s not exists" % name)

    def mod(self):
        return self.cur.get_mod()

    def cur_name(self):
        return str(self.cur)

    def set_ice_mod(self, name):
        if len(self.__path) == 2:
            mod = __import__(name, globals())
        else:
            pre = self.__path[-2]._ice_mod
            mod = getattr(pre, name)

        self["_ice_mod"] = mod


def stack_ctx(func):
    @wraps(func)
    def build(self, ctx):
        ctx.push(self)

        mod = func(self, ctx)

        ctx.pop()
        return mod

    return build

