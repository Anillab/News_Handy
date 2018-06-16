from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news_sources
from ..models import News_Sources
@main.route('/')
def index():
    '''
    news_sources_results_list
    '''
    pass
