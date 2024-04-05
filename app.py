from flask import Flask, render_template
from faker import Faker # ← not sure
import random, os, sys

sys.path.insert(0, '/home/nansp/knyofu/scripting')

from mmntb import Mmntb

mmntb = Mmntb()

app = Flask(__name__)

@app.route('/')
def index():
    template_dir_path = os.getcwd() + '/templates/indexes'
    indexes = os.listdir(template_dir_path)
    index = random.choice(indexes)
    return render_template(f"indexes/{index}")

@app.route('/mmntb/')
def mmntbm():
    idList=mmntb.idgen()
    status=mmntb.statusgen()
    template=mmntb.choose_template(status)
    if status == 'functional':
        statrelinfo_=mmntb.act_with_status(status)
        statrelinfo = statrelinfo_[0]
        situation = statrelinfo_[1]
        family_situation = situation[0]
        opinion = situation[1]
        if opinion == 'unable':
            opinion_cons = mmntb.opinion_cons(opinion)
        elif opinion == 'unconvenient':
            opinion_cons = mmntb.opinion_cons(opinion)
        elif opinion == 'likely to stay':
            opinion_cons = mmntb.opinion_cons(opinion) 
        elif opinion == 'good':
            opinion_cons = mmntb.opinion_cons(opinion)
    elif status == 'enemy':
        statrelinfo = mmntb.act_with_status(status)
        family_situation = ""
        opinion = ""
        opinion_cons = ""

    else:
        statrelinfo=mmntb.act_with_status(status)
        family_situation = ''
        opinion = ''
        opinion_cons = ''

    
    return render_template(template, idList=idList, status=status, statrelinfo=statrelinfo, familysit=family_situation, opinion=opinion, opinion_cons=opinion_cons)

if __name__ == '__main__':
    app.run(debug=True)

