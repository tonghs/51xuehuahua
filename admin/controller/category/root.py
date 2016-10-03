#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminHandler
from misc._route import route


@route('/category')
class Index(AdminHandler):
    def get(self):
        self.render()


@route('/category/add')
class Add(AdminHandler):
    def get(self):
        self.render()
