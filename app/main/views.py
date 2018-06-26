from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_news_sources,get_news_articles
from ..models import News_Sources,News_Article
@main.route('/')
def index():
    '''
    a function that displays the main route page
    '''
    news_sources=get_news_sources('general')
    xxx=get_news_sources('sports')
    business=get_news_sources('business')

    # print(news_sources)
    return render_template('index.html',general=news_sources,sports=xxx,business=business)

@main.route('/sources/<id>')
@main.route('/articles')
def articles(id):
    '''
    '''
    source_articles=get_news_articles('id')

    return render_template('articles.html',articles=source_articles)
