from flask import Flask, render_template,request
import requests


app = Flask(__name__)

URL = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
r = requests.get(url = URL)
data = r.json()
explanation = data['explanation']
date = data['date']
photographer = data['copyright']
title = data['title']
img_url = data['hdurl']

@app.route('/')
def home():
    return render_template('index.html', explanation=explanation, date=date, photographer=photographer, title=title, img_url=img_url)

if __name__ == "__main__":
    app.run(debug=True)