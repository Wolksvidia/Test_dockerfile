# -*- coding: utf-8 -*-

DB_URL = 'postgresql://postgres:postgres@postgres/inventory'


class Config(object):
    SECRET_KEY = 'estasdelachingadamano'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'mi_cuenta_@gmail.com'
    MAIL_PASSWORD = 'Password'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DB_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
