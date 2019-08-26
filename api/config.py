# 適当
import os
from datetime import timedelta

class DevelopmentConfig:

    DEBUG = True
    JSON_AS_ASCII = False
    REMEMBER_COOKIE_DURATION = timedelta(hours=1)

    db_user = os.getenv('DB_USERNAME', 'root')
    db_password = os.getenv('DB_PASSWORD', 'root')
    db_name = os.getenv('DB_NAME', None)

    host = '127.0.0.1'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(
        db_user, db_password, host, db_name)

    SQLALCHEMY_POOL_RECYCLE = 90
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 3,
    }

Config = DevelopmentConfig
