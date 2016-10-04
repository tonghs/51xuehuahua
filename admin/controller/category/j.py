#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from controller._base import AdminJsonBaseHandler
from misc._route import route


@route('/j/category')
class Category(AdminJsonBaseHandler):
    def post(self):
        self.finish()
