from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news_sources
from ..models import News_Sources
@main.route('/')
def index():
    '''
    a function that displays the main route page
    '''

    news_sources=get_news_sources('sources')
    print(sources)
    return render_template('index.html',sources=news_sources)
