#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
# from model._base import drop_table, init_db
# from model.user import User
from model.captcha import Captcha
from model.local_auth import LocalAuth
import hashlib


def main():
    # drop_table()
    # init_db()

    data = dict(
        user_id=1,
        user_name="tonghs",
        password=hashlib.md5('admin').hexdigest(),
    )
    LocalAuth.create(**data)


def test_captcha():
    for i in range(10):
        print Captcha.captcha_new()

if __name__ == '__main__':
    test_captcha()
