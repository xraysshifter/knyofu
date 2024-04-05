from faker import Faker
import random, nltk
from data import *
from nltk.corpus import words
from faker import config

class Mmntb:

    def __init__(self):
        #faker initialization:
        avail_locales = config.AVAILABLE_LOCALES
        self.f=Faker(avail_locales)
        self.ex_reas = random.choice(exile_reasons)
        print(self.ex_reas)
        
        #method specific initialization:
        
    def idgen(self):
        nltk.download('words')
        wordlist=words.words()
        self.name = self.f.name_nonbinary()
        self.address = self.f.address()
        self.serial_n = self.f.sha1() 
        idList=[self.name, self.address, self.serial_n]

        return idList

    def statusgen(self):
        self.statusList = ['unknown', 'functional', 'exiled', 'pent', 'enemy']
        self.status = random.choice(self.statusList)

        return self.status

    def choose_template(self, status):
        self.template_folder_path = "mmntb"
        self.template_name = status + '.html'
        self.template = self.template_folder_path + '/' + self.template_name 

        return self.template

    def act_with_status(self, status):
        if status:
            self.status_op=getattr(self, status)

        return self.status_op()
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!STATUS OPERATIONS!!!!!!!!!!!!!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def exiled(self):
        self.exile_reason = random.choice(exile_reasons)

        return self.exile_reason

    def unknown(self):
        self.last_seen = self.f.past_date()

        return self.last_seen
    
    def functional(self):
        self.function = random.choice(function_department)
        self.situation = [random.choice(family_situation), random.choice(opinion)]

        return self.function, self.situation

    def opinion_cons(self, opinion):
        if opinion == 'unable':
            string = 'will be exiled the '
            self.cons = string + str(self.f.future_date()) + ' if subject didn\'t upgrade until his last test happening the ' + str(self.f.future_date())
        elif opinion == 'unconvenient':
            string = 'another test will be passed the: '
            self.cons = string + str(self.f.future_date())
        elif opinion == 'good':
            self.cons = 'some test will be passed next month'
        else : 
            self.cons = 'some test will be passed next three month'

        return self.cons

    def pent(self):
        self.corridor = random.choice(corridors)
        self.level = str(random.randint(1, 25))
        self.penitentiary = random.choice(penitentiaries)
        self.current_loc = self.level + ', ' + self.corridor
        print(self.current_loc)
        self.room_number = random.randint(50, 999)
        self.reason = random.choice(exile_reasons)

        print(self.current_loc)

        return self.penitentiary, self.current_loc, self.reason, self.room_number

    def enemy(self):
        self.witnessed = random.choice(witnessed)
        self.last_seen = self.f.past_date()

        return self.witnessed, self.last_seen 
