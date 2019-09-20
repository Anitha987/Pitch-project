import os
class config :
  '''
  Genarate configuration parent class
  '''

  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:1234@localhost/pitch'
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = True
class TestConfig(Config):
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:1234@localhost/pitch_test'
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}    

