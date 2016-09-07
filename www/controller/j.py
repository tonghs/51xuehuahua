#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from _base import JsonBaseHandler
from misc._route import route
from model.local_auth import LocalAuth


@route('/j/login')
class Login(JsonBaseHandler):
    def post(self):
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')

        form = LocalAuth.Form(**self.arguments)
        if form.validate():
            try:
                local_auth, user = LocalAuth.login(user_name, password)
                if user:
                    user_dict = dict(
                        id=user.id,
                        name=user.name
                    )
                    self.set_secure_cookie("user", json.dumps(user_dict))
                    result = dict(result=True, msg="")
                else:
                    result = dict(result=False, user_name="用户名密码错误")

            except LocalAuth.DoesNotExist:
                result = dict(result=False, user_name="用户不存在")

        else:
            result = form.errors
            result.update(result=False)

        self.finish(result)
