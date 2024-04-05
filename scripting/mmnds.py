from faker import Faker
from faker import config

class Mmnds:
    def __init__(self, status):
        avail_locales = config.AVAILABLE_LOCALES
        self.f = Faker(avail_locales)
        self.status = status
        
        if self.status == 'unkown':
        if self.status == 'enemy':
        if self.status == 'pent':
        if self.status == 'functional':
        if self.status == 'exiled':

    def last_infos(self, status):
        if status == "enemy":
        if status == "unkown":
