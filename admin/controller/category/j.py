#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminJsonBaseHandler
from misc._route import route
from peewee import IntegrityError

from model.category import Category


@route('/j/category')
class CategoryHandler(AdminJsonBaseHandler):
    def post(self):
        form = Category.Form(**self.arguments)

        if form.validate():
            try:
                Category.create(**self.arguments)
            except IntegrityError:
                result = dict(result=False, name="分类名称已经存在")
            else:
                result = dict(result=True)
        else:
            result = dict(result=False)
            result.update(form.errors)

        self.finish(result)
