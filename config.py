import os
class Config:
    '''
    This is ageneral configuration class
    '''
    news_sources_api_base_url='https://newsapi.org/v2/sources?category={}&apiKey={}'
    news_article_url='https://newsapi.org/v2/everything?q={}&apiKey={}'
    news_api_key=os.environ.get('news_api_key')
    secret_key=os.environ.get('secret_key')

class ProdConfig(Config)
    pass
class DevConfig(Config):
    DEBUG= True
config_options={
'development':DevConfig,
'production':ProdConfig
}#this is a dictonary
