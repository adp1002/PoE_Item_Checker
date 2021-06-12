import requests
import json
import util
import equipment
import csv

class Stash:

    def __init__(self, desired_mods):
        self.__num_tabs = 0
        self.__stash = []
        self.BASETYPES_FILE = 'base_items.csv'
        self.__basetypes = set()
        self.__good_equipment = []
        self.__desired_mods = util.parse_explicit_mods(desired_mods)


    def get_stash(self):
        return self.__stash

    def get_good_equipment(self):
        return self.__good_equipment

    def load_basetypes(self):
        with open(self.BASETYPES_FILE, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                self.__basetypes.add(row[1]) # 2nd column is the basetype name e.g. Siege Axe

    def load_stash(self, session, acc_name, league):
        self.__num_tabs = session.post('https://pathofexile.com/character-window/get-stash-items?league=' + league + '&accountName=' + acc_name).json()['numTabs']

        for i in range(self.__num_tabs):
            self.__stash.append(session.post('https://www.pathofexile.com/character-window/get-stash-items?accountName=' +
                                acc_name + '&realm=pc&league=' + league + '&tabIndex=' + str(i)).json()['items'])
        self.load_basetypes()
        self.select_equipment()
        
        #print(json.dumps(self.__stash[6], indent=2, sort_keys=True))


    def select_equipment(self):
        for tab in self.__stash:
            for item in tab:
                try:
                    if item['baseType'] in self.__basetypes:
                        equip = equipment.Equipment(item['name'], item['baseType'], item['inventoryId'], item['explicitMods'])
                        #print([item['name'], item['baseType'], item['inventoryId'], item['explicitMods']])
                        #print(json.dumps(item, indent=2, sort_keys=True))
                        if self.check_equipment(equip):
                            self.__good_equipment.append(equip.get_name())
                except KeyError:
                    pass

    def check_equipment(self, equip):
        explicit_mods = equip.get_explicit_mods()

        if set(self.__desired_mods).issubset(set(explicit_mods)):
            for mod_string in self.__desired_mods.keys():
                if self.__desired_mods[mod_string] > explicit_mods[mod_string]: #TODO The '<' operator should be user defined.
                    return False
            return True
        else:
            return False