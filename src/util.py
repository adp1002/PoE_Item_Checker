import re

def parse_explicit_mods(explicit_mods):
        tmp_dict = dict()

        for mod in explicit_mods:
            mod_value = re.findall(r'\d+', mod)
            # For mods that have multiple numbers e.g. Adds # to # fire damage to attacks
            if mod_value:
                if len(mod_value) > 1:
                    tmp_value = 0
                    for value in mod_value:
                        tmp_value += int(value)
                    mod_value = tmp_value//len(mod_value)
                else:
                    mod_value = int(mod_value[0])

                mod_string = re.sub(r'\d+','{0}', mod)
                tmp_dict[mod_string] = mod_value

        return tmp_dict