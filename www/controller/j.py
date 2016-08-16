#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from _base import JsonBaseHandler
from misc._route import route
from model.user import User


@route('/j/login')
class Login(JsonBaseHandler):
    def post(self):
        user = self.get_argument('username')
        pwd = self.get_argument('password')

        user_ = User.login(user, pwd)
        if user_:
            user_dict = dict(
                user=user,
                name=user_.name
            )
            self.set_secure_cookie("user", json.dumps(user_dict))
            ret = dict(login=True, msg="")
        else:
            ret = dict(login=False, msg="用户名密码错误")

        self.finish(ret)


@route('/j/user/reset_pwd')
class Pwd(JsonBaseHandler):
    def post(self):
        pwd = self.get_argument('pwd')
        new_pwd = self.get_argument('new_pwd')
        re_pwd = self.get_argument('re_pwd')

        ret = dict(result=False, msg="")

        if pwd and new_pwd and re_pwd:
            if new_pwd == re_pwd:
                user = User.login(self.current_user.user, pwd)
                if user:
                    user.reset(new_pwd)
                    ret = dict(result=True, msg="修改成功！")
                else:
                    ret = dict(result=False, msg="原密码输入错误！")

            else:
                ret = dict(result=False, msg="两次输入密码不一致！")
        else:
            ret = dict(result=False, msg="全部为必填项不可为空！")

        self.finish(ret)
