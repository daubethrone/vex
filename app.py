#Importing dependencies
from flask import Flask, render_template
import json

#Importing json data
with open('national-flags_national-flags_captured-list_2025-02-20_17-30-12_d06e83e0-1abf-4b77-9098-d94171c1ce17.json', 'r') as database:
    data = json.load(database)

app = Flask(__name__)

class Country:
    def __init__(country,flag,summary,adopt,desc):
        self.country = country
        self.flag = flag
        self.summary = summary
        self.adopt = adopt
        self.desc = desc

@app.route('/test')
def get_random() :
    id = randint(1,len(data.keys())/7) # Ranges from 1 to last json country
    country = data[id].get('Country Name')
    flag = data[id].get('Flag Image')
    summary = data[id].get('Flag Description')
    adopt = data[id].get('Adoption Date')
    desc = data[id].get('Flag Description')
    return Country(country,flag,summary,adopt,desc)


@app.route('/')
def welcome() :
    return render_template('welcome.html')

