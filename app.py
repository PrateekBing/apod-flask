from flask import Flask, render_template,request
import requests
from datetime import date, timedelta, datetime



app = Flask(__name__)

today = date.today()
DD = timedelta(days=1)
yesterday = today-DD

api_key = 'LkTRbzh08wc2q7mEDm80MzWV2fsmQq1hWDDvgkq1'


URL = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={yesterday}'
r = requests.get(url = URL)
data = r.json()
explanation = data['explanation']

date = data['date']
title = data['title']
img_url = data['hdurl']

@app.route('/')
def home():
    return render_template('index.html', explanation=explanation, date=date, title=title, img_url=img_url)

if __name__ == "__main__":
    app.run(debug=True)
    