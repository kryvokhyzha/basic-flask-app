import os


NEW_ENV = os.environ.get('ENV_NAME', 'default_value')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'MY_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False