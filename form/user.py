#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, validators
from wtforms import TextField


class UserForm(Form):
    name = TextField('name', [validators.Length(max=64, message="姓名最多允许 64 个字符"),
                              validators.DataRequired()])
    phone = TextField('phone', [validators.Optional(), validators.Regexp('\d{11}', message="电话格式错误")])
    email = TextField('email', [validators.Optional(), validators.Email(message="邮箱格式错误")])
