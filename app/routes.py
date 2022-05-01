from flask import render_template
from app import app
from .request import get_head_news


@app.route('/')
@app.route('/home')
def home_page():
    
   
    return render_template('home.html')