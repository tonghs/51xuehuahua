#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from _base import AdminJsonBaseHandler
from misc._route import route

from model.admin import Admin
from model.qiniu import QINIU_TOKEN
from model._base import R


@route('/j/login')
class Login(AdminJsonBaseHandler):
    def post(self):
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')

        admin = Admin.login(user_name, password)
        if admin:
            admin_dict = dict(
                user_name=user_name,
                name=admin.name
            )
            self.set_secure_cookie("admin", json.dumps(admin_dict))
            result = dict(result=True, msg="")
        else:
            result = dict(result=False, password="用户名密码错误")

        self.finish(result)


@route('/j/user/reset_pwd')
class Pwd(AdminJsonBaseHandler):
    def post(self):
        pwd = self.get_argument('pwd')
        new_pwd = self.get_argument('new_pwd')
        re_pwd = self.get_argument('re_pwd')

        ret = dict(result=False, msg="")

        if pwd and new_pwd and re_pwd:
            if new_pwd == re_pwd:
                user = Admin.login(self.current_user.user, pwd)
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


@route('/j/qiniu_token')
class QiniuToken(AdminJsonBaseHandler):
    def get(self):
        self.finish(dict(uptoken=QINIU_TOKEN.new(
            returnBody="""{
                "key":$(key),
                "w": $(imageInfo.width),
                "h": $(imageInfo.height),
                "fn": $(fname)
            }""",
            saveKey=str(R.gid()))))
