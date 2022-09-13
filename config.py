from os import path, getenv
from dotenv import load_dotenv
import os

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    FLASK_DEBUG = getenv('FLASK_DEBUG')
    PREFIX = getenv('PREFIX')
