import util

class Equipment:

    def __init__(self, name, base_type, inventory_id, explicit_mods):
        self.__name = name
        self.__base_type = base_type
        self.__inventory_id = inventory_id
        self.__explicit_mods = dict()
        self.__explicit_mods = util.parse_explicit_mods(explicit_mods)

    def get_name(self):
        return self.__name

    def get_base_type(self):
        return self.__base_type

    def get_inventory_id(self):
        return self.__inventory_id

    def get_explicit_mods(self):
        return self.__explicit_mods

    def __str__(self):
        return self.__name