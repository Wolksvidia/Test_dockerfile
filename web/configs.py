# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'estasdelachingadamano'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'mi_cuenta_@gmail.com'
    MAIL_PASSWORD = 'Password'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres/inventory'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
