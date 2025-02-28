#Importing dependencies
from flask import Flask, render_template
import json
import random
app = Flask(__name__)

with open('national-flags_national-flags_captured-list_2025-02-20_17-30-12_d06e83e0-1abf-4b77-9098-d94171c1ce17.json', 'r') as database:
    data = json.load(database)
item_count = len(data)
numb = 0

class Flag:
    def __init__(self, numb, date, flag, country, wikipedia, summary):
        self.flag_id = numb
        self.date = date
        self.flag = flag
        self.country = country
        self.wikipedia = wikipedia
        self.summary = summary
    
flag_list = []
flag_list = []
for numb, item in enumerate(data):
    flag_list.append(Flag(
        numb, 
        item["Adoption Date"],  
        item["Flag Image"],     
        item["Country Name"],   
        item["Flag Page Link"], 
        item["Flag Description"]
    ))




@app.route('/') # Home
def pick_flag() :
    picked_flag = random.choice(flag_list)
    pdate = picked_flag.date
    pflag = picked_flag.flag
    pcountry = picked_flag.country
    psummary = picked_flag.summary
    pwikipedia = picked_flag.wikipedia
    return render_template('homepage.html', date=pdate, flag=pflag, country=pcountry, summary=psummary, wikipedia=pwikipedia)

def random_username() : # Random Skyblog Username
    return random.choice(['xX_DarkSoul_Xx', 'EmoTears69', 'BloodyHeart_x3', 'BrokenAngel77', 'DeathKisses_xX', 'ToxicLullaby', 'Shadow_Lover13', 'ScreamingSilence', 'CryBaby_xo'])
        
@app.route('/skyblog') # Skyblog UI
def skyblog() :
        usr = random_username()
        picked_flag_sk = random.choice(flag_list)
        pdate_sk = picked_flag_sk.date
        pflag_sk = picked_flag_sk.flag
        pcountry_sk = picked_flag_sk.country
        psummary_sk = picked_flag_sk.summary
        pwikipedia_sk = picked_flag_sk.wikipedia
        return render_template('skyblog.html', date=pdate_sk, flag=pflag_sk, country=pcountry_sk, summary=psummary_sk, wikipedia=pwikipedia_sk, usr=usr)


if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5001, debug=True)
