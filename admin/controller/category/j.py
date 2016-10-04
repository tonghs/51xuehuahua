#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminJsonBaseHandler
from misc._route import route
from peewee import IntegrityError

from model.category import Category


@route('/j/category')
class CategoryHandler(AdminJsonBaseHandler):
    def get(self):
        id = self.get_argument('id', 0)
        category = dict()

        if id:
            try:
                category = Category.get(Category.id == id)
                category = category.to_dict()
            except Category.DoesNotExist:
                category = dict()

        self.finish(category)

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


@route('/j/category/list')
class CategoryListHandler(AdminJsonBaseHandler):
    def get(self):
        page = self.get_argument('page', '1')
        if page.isdigit():
            page = int(page)

        limit = self.get_argument('limit', 20)

        li, count, total_page = Category.list(page, limit)
        li = [o.to_dict(extra_attrs=['parent_']) for o in li]

        self.finish(dict(li=li, count=count,
                         total_page=total_page,
                         page=page, limit=limit))


@route('/j/category/top')
class Top(AdminJsonBaseHandler):
    def get(self):
        li = Category.top()
        li = [o.to_dict() for o in li]

        self.finish(dict(li=li))


@route('/j/category/edit')
class Edition(AdminJsonBaseHandler):
    def post(self):
        id = self.get_argument('id', 0)
        result = dict(result=False)

        if id:
            try:
                category = Category.get(Category.id == id)
                for k, v in self.arguments.iteritems():
                    if hasattr(category, k):
                        setattr(category, k, v)

                category.save()

            except Category.DoesNotExist:
                result = dict(result=False)
            else:
                result = dict(result=True)

        self.finish(result)


@route('/j/catagory/rm')
class _(AdminJsonBaseHandler):
    def post(self):
        id = self.get_argument('id', 0)
        result = dict(result=False)

        if id:
            try:
                category = Category.get(Category.id == id)
                category.delete_instance()
            except Category.DoesNotExist:
                result = dict(result=False)
            else:
                result = dict(result=True)

        self.finish(result)
