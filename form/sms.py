#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, validators
from wtforms import TextField


class SMSForm(Form):
    user_name = TextField('user_name', [validators.DataRequired(message="请输入手机号码"),
                                        validators.Regexp('\d{11}', message="手机号码格式错误")])
    token = TextField('token', [validators.DataRequired(message="请输入图片验证码")])
