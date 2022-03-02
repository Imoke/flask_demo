# -*- coding: utf-8 -*-
import datetime
import os

from marshmallow_peewee import *
from peewee import *
from playhouse.flask_utils import FlaskDB

from package.base.app import webapp

if os.environ.get('FLASK_ENV') == 'development':
    import logging
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

# 会被存入webapp.config供FlaskDB使用
# DATABASE = 'postgresql://pgsql:Dpp-pgsql123%23%23@pgsql-service.platform:5432/testdb'

DATABASE = { "name":"testdb",
             "engine": "PostgresqlDatabase",
             "user": "pgsql",
             "password": "Dpp-pgsql123##",
             "port": 5432,
             "host": "pgsql-service.platform"}

# 将当前文件的以大写字母开头的字符串存入webapp.config
webapp.config.from_object(__name__)

flask_db = FlaskDB(webapp)

database = flask_db.database
