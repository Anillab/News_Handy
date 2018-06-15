import os
class Config:
    '''
    This is ageneral configuration class
    '''
    pass
class ProdConfig(Config)
    pass
class DevConfig(Config):
    DEBUG= True
config_options={
'development':DevConfig,
'production':ProdConfig
}#this is a dictonary
