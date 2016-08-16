#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa

from _base import BaseHandler, LoginHandler
from misc._route import route

from model.cata import Cata

from service.service import get_template_dict


@route('/login')
class Login(BaseHandler):
    def get(self):
        self.render()


@route('/')
class Index(LoginHandler):
    def get(self):
        d = get_template_dict()
        for cata in Cata.select():
            d[cata.cata][cata.source] = dict(cata=cata.cata_cn, view=cata.view)
        self.render(data=d)


@route('/logout')
class Logout(LoginHandler):
    def get(self):
        self.clear_cookie('user')
        self.redirect('/')
