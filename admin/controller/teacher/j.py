#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import json
from controller._base import AdminJsonBaseHandler
from misc._route import route

from model.teacher import Teacher


@route('/j/teacher')
class TeacherHandler(AdminJsonBaseHandler):
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


@route('/j/teacher/list')
class TeacherList(AdminJsonBaseHandler):
    def get(self):
        page = self.get_argument('page', '1')
        if page.isdigit():
            page = int(page)

        limit = self.get_argument('limit', 20)

        li, count, total_page = Teacher.list(page, limit)
        li = [o.to_dict(extra_attrs=['method', 'category', 'avatar_']) for o in li]

        self.finish(dict(li=li, count=count,
                         total_page=total_page,
                         page=page, limit=limit))
