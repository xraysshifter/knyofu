from faker import Faker
import random
from data import *

class Mmntb:

    def __init__(self):
        #faker initialization:
        self.f=Faker(['it_IT', 'en_US', 'ja_JP', 'fr_FR'])
        self.ex_reas = random.choice(exile_reasons)
        print(self.ex_reas)
        
        #method specific initialization:
        
    def idgen(self):
        self.name = self.f.name_nonbinary()
        self.address = self.f.address()
        self.email = self.f.ascii_email()

        idList=[self.name, self.address, self.email]

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
        pass

    def enemy(self):
        pass
        





    

    
