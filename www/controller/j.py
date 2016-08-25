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
            local_auth, user = LocalAuth.login(user_name, password)

            if user:
                user_dict = dict(
                    user=user,
                    name=user.name
                )
                self.set_secure_cookie("user", json.dumps(user_dict))
                result = dict(reault=True, msg="")
            else:
                result = dict(reault=False, msg="用户名密码错误")
        else:
            result = form.errors
            result.update(result=False)

        self.finish(result)
