import os
from os.path import join, dirname, realpath

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join('app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
FIXTURES_DIRS = join(dirname(realpath(__file__)), 'fixtures')