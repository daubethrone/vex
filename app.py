#Importing dependencies
from flask import Flask, render_template
import json
import random
app = Flask(__name__)

#Importing json data
with open('national-flags_national-flags_captured-list_2025-02-20_17-30-12_d06e83e0-1abf-4b77-9098-d94171c1ce17.json', 'r') as database:
    data = json.load(database)
item_count = len(data)
num = random.randint(1,item_count)
date = data[num]["Adoption Date"]
flag = data[num]["Flag Image"]
country = data[num]["Country Name"]
wikipedia = data[num]["Flag Page Link"]
summary = data[num]["Flag Description"]
#check how to implement summary and wikipedia link

@app.route('/') #Original route, html only
def random_flag(date=date, flag=flag, country=country, summary=summary, wikipedia=wikipedia) :
    return render_template('mainpage.html', date=date, flag=flag, country=country, summary=summary, wikipedia=wikipedia)

@app.route('/new') #New CSS-styled route
def random_flag_two(date=date, flag=flag, country=country, summary=summary, wikipedia=wikipedia) :
    return render_template('new.html', date=date, flag=flag, country=country, summary=summary, wikipedia=wikipedia)

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port='5001', debug=True)