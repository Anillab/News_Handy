from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news_sources
from ..models import News_Sources
@main.route('/')
def index():
    '''
    a function that displays the main route page
    '''
    sources='hhhhhahahahha'
    return render_template('index.html',sources=sources)
