
class Context:
    def __init__(self, parent=None):
        self.parent = parent
        self.types = {}

    def get_type(self, item_type):
        pass

    def update_sub_mod(self, mods):
        pass
