import requests
import json
import stash
import util

class AccountInfo:

    def __init__(self, sess_id, acc_name, league):
        self.__POESESSID = sess_id
        self.__acc_name = acc_name
        self.__league = league

    def get_acc_name(self):
        return self.__acc_name

    def get_session(self):
        return self.__session

    def get_league(self):
        return self.__league

    def set_session_cookies(self):
        self.__session = requests.Session()
        self.__session.headers.update({'user-agent': 'g.Vc'})
        self.__session.cookies.set('POESESSID', self.__POESESSID, domain='pathofexile.com', path='/')
        num_tabs = self.__session.post('https://pathofexile.com/character-window/get-stash-items?league=standard&accountName=CaseR').json()['numTabs']

        tab_1 = self.__session.post('https://www.pathofexile.com/character-window/get-stash-items?accountName=' + self.__acc_name + '&realm=pc&league=ssf+ritual&tabIndex=1').json()['items']

desired_mods = {'+10% to Fire Resistance', '+10% to Cold Resistance', '+60 to maximum Life'}

POESESSID = None #You can get it from the cookies after you've logged in PoE website
ACC_NAME = None
LEAGE = None

acc = AccountInfo(POESESSID, ACC_NAME, POESESSID,)
acc.set_session_cookies()

s = stash.Stash(desired_mods)
s.load_stash(acc.get_session(), acc.get_acc_name(), acc.get_league())
print(s.get_good_equipment())