#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminJsonBaseHandler
from misc._route import route

from model.teacher import Teacher


@route('/j/teacher')
class CategoryHandler(AdminJsonBaseHandler):
    def post(self):
        form = Teacher.Form(**self.arguments)

        if form.validate():
            Teacher.create(**self.arguments)
            result = dict(result=True)
        else:
            result = dict(result=False)
            result.update(form.errors)

        self.finish(result)
