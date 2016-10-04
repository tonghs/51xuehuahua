#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import redis as redis_

from pub_config import MYSQL, REDIS
from peewee import Model, MySQLDatabase

from playhouse.shortcuts import model_to_dict, dict_to_model

db = MySQLDatabase(MYSQL.DB, user=MYSQL.USER, password=MYSQL.PWD, host=MYSQL.HOST)
redis = redis_.StrictRedis(host=REDIS.HOST, port=REDIS.PORT, db=REDIS.DB)


class Base(Model):

    def to_dict(self):
        return model_to_dict(self)

    @classmethod
    def from_dict(cls, d):
        return dict_to_model(cls, d) if d else None

    class Meta:
        database = db


def init_db():
    from model.user import User
    from model.local_auth import LocalAuth
    from model.admin import Admin
    from model.category import Category

    # 创建表
    # db.create_tables([User, LocalAuth])
    # db.create_tables([Admin])
    db.create_tables([Category])


def drop_table():
    from model.user import User
    from model.local_auth import LocalAuth

    db.drop_tables([User, LocalAuth])


class RedisUtil(object):
    ''' Redis 获取 key
        根据调用方法名自动生成 key name
    '''
    def __getattr__(self, name):
        def _get_key(param=''):
            return '{name}{param}'.format(name=name.upper(), param=param)

        return _get_key

R = RedisUtil()
