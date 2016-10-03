#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wtforms import Form, validators
from wtforms import TextField


class CategoryForm(Form):
    name = TextField('name', [validators.DataRequired(message="请输入分类名称"),
                              validators.Length(max=32, message="分类名称最多允许 32 个字符")])
