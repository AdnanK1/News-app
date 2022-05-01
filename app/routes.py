from flask import render_template
from app import app
from .request import get_news

@app.route('/')
@app.route('/home')
def home_page():
    contents = get_news
    return render_template('home.html', articles=contents)