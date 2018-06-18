import urllib.request,json
from .models import News_Sources,News_Article
api_key=None
base_url=None
def configure_request(app):
    '''
    a function that takes in the application instance and replaces the value of variables set to none
    '''
    global api_key,base_url,news_article_url
    api_key=app.config['news_api_key']
    base_url=app.config['news_sources_api_base_url']
    news_article_url=app.config['news_article_url']

def get_news_sources(category):
    '''
    a function that gets the json response to our url request
    '''
    get_news_sources_url=base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_sources_url) as url:
        get_news_sources_data=url.read()
        get_news_sources_response=json.loads(get_news_sources_data)
        news_sources_results=None
        if get_news_sources_responose['results']:
            news_sources_results_list=get_news_sources_response['results']
            news_sources_results=process_sources_results(news_sources_results_list)
            return news_sources_results
def process_sources_results(news_sources_list):

    '''
    '''
    news_sources_results=[]
    for source in news_sources_list:
        id=source.get('id')
        title=source.get('title')
        author=sorce.get('url')
        urlToImage=source.get('urlToImage')
        description=source.get('description')
        publishedAt=source.get('publishedAt')
        news_object=News_Sources(id,title,url,urlToImage,description,publishedAt)
        news_sources_results.append(news_object)
    return news_sources_results
