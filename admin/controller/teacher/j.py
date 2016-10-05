#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import json
from controller._base import AdminJsonBaseHandler
from misc._route import route

from model.teacher import Teacher


@route('/j/teacher')
class CategoryHandler(AdminJsonBaseHandler):
    def post(self):
        args = json.loads(self.request.body)
        method = args.get('method')
        category = args.get('category')

        form = Teacher.Form(**args)
        if form.validate():
            del args['method']
            del args['category']
            teacher = Teacher.create(**args)
            teacher.set_method(method)
            teacher.set_category(category)

            result = dict(result=True)
        else:
            result = dict(result=False)
            result.update(form.errors)

        self.finish(result)
