#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
from model._base import drop_table, init_db
from model.user import User
from model.admin import Admin
from model.captcha import Captcha
from model.sms import SMS
from model.local_auth import LocalAuth
import hashlib


def main():
    drop_table()
    init_db()


def test_captcha():
    for i in range(10):
        print Captcha.captcha_new()


def test_sms_code():
    # print SMS.new(18601980445)
    print SMS.verify(18601980445, '3768')


def test_local_auth():
    LocalAuth.create(user_id=1, user_name=18848588586, password='ataa')

if __name__ == '__main__':
    init_db()
    Admin.create(name='tonghs', user_name='admin',
                 password=hashlib.md5('admin').hexdigest())
