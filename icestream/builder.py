import os
from .iceyacc import parse
from .context import *


def build(file_name):
    mod_name = os.path.basename(file_name).replace('.', '_').rsplit('_', 1)[0]
    ctx = Context(mod_name)
    for item in parse(file_name):
        item.build(ctx)
    return ctx.mod()

