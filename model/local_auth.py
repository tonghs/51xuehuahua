#!/usr/bin/env python
# -*- coding: utf-8 -#-

import hashlib
from model._base import Base
from model.user import User
from peevww import CharField, PrimaryKeyField, TimeField

from form.local_auth import LocalAuthForm


class LocalAuth(Base):
    user_id = PrimaryKeyField()
    user_name = CharField()
    password = CharField()
    creation_time = TimeField()

    class Meta:
        indexes = ((('user_name', 'password'), True),)

    @classmethod
    def login(cls, user_name, password):
        user = None
        local_auth = None
        try:
            local_auth = LocalAuth.get(LocalAuth.user_name == user_name, LocalAuth.password == hashlib.md5(password).hexdigest())
            user_id = local_auth.user_id

            user = User.get(User.user_id == user_id)

        except LocalAuth.DoesNotExist:
            # 用户不存在
            pass

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
