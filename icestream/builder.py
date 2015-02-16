import os
from .iceyacc import parse
from .context import *


class FileLocator:
    def __init__(self, *paths):
        self.paths = ['./'] + list(paths)

    def read(self, file_name):
        for p in self.paths:
            file_path = os.path.join(p, file_name)
            try:
                return open(file_path).read()
            except:
                continue
        raise IOError("%s not found." % file_name)


gen_slice_cmd = lambda file_name, *paths: "--all %s %s" % (" ".join(["-I %s" % p for p in paths]), file_name)


def build(file_name, *paths):
    import Ice
    slice_cmd = gen_slice_cmd(file_name, *paths)
    Ice.loadSlice(slice_cmd)

    mod_name = os.path.basename(file_name).replace('.', '_').rsplit('_', 1)[0]
    ctx = Context(mod_name)
    locator = FileLocator(*paths)

    for item in parse(file_name, locator):
        item.build(ctx)

    return ctx.mod()

