#!/usr/bin/env python
# -*- coding: utf-8 -*-


from wtforms import Form, validators
from wtforms.fields import TextField


class LocalAuthForm(Form):
    user_name = TextField('user_name', [validators.DataRequired(message="用户名不可为空")])
    password = TextField('password', [validators.DataRequired(message="密码不可为空")])
