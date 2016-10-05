#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminHandler
from misc._route import route

from model.category import Category


@route('/teacher')
class Index(AdminHandler):
    def get(self):
        category = Category.sub()
        self.render(category=category)
