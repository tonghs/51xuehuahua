#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from model._base import Base
from model.user import User
from peewee import CharField, PrimaryKeyField, TimeField

from form.local_auth import LocalAuthForm


class LocalAuth(Base):
    user_id = PrimaryKeyField()
    user_name = CharField()
    password = CharField()
    creation_time = TimeField()

    class Meta:
        indexes = ((('user_name', 'password'), True),)
        db_table = 'local_auth'

    @classmethod
    def exists(cls, user_name):
        local_auth = LocalAuth.get(LocalAuth.user_name == user_name)
        return local_auth

    @classmethod
    def login(cls, user_name, password):
        local_auth = LocalAuth.get(LocalAuth.user_name == user_name, LocalAuth.password == hashlib.md5(password).hexdigest())
        user_id = local_auth.user_id

        user = User.get(User.id == user_id)

        return local_auth, user

    def reset(self, new_pwd):
        ''' 重置密码
            params:
                user: 用户名
                new_pwd: 新密码
        '''
        self.password = hashlib.md5(new_pwd).hexdigest()
        self.save()

    Form = LocalAuthForm
