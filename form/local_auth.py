#!/usr/bin/env python
# -*- coding: utf-8 -*-


from wtforms import Form, validators
from wtforms.fields import TextField


class LocalAuthForm(Form):
    user_name = TextField('user_name', [validators.DataRequired(message="用户名不可为空")])
    password = TextField('password', [validators.DataRequired(message="密码不可为空")])


class RegForm(Form):
    user_name = TextField('user_name', [validators.DataRequired(message="手机号码不可为空"),
                                        validators.Regexp('\d{11}', message="手机号码格式错误")])
    password = TextField('password', [validators.DataRequired(message="密码不可为空")])
    sms_code = TextField('sms_code', [validators.DataRequired(message="动态验证码不可为空")])
