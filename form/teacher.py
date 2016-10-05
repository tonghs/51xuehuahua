#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, validators
from wtforms import StringField, FieldList


class TeacherForm(Form):
    avatar = StringField('avatar', [validators.DataRequired(message="请上传头像")])
    name = StringField('name', [validators.DataRequired(message="请填写姓名"),
                                validators.Length(max=64, message="姓名最多允许 64 个字符")])
    category = FieldList(StringField('category', [validators.DataRequired(message="请选择擅长领域")]), min_entries=1)
    method = FieldList(StringField('method', [validators.DataRequired(message="请选择授课方式")]), min_entries=1)
    desc = StringField('desc', [validators.DataRequired(message="请填写讲师介绍")])
