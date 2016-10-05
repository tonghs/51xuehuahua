#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import hashlib
from model._base import drop_table, init_db
from model.admin import Admin
from model.teacher import Teacher


def main():
    # drop_table()
    init_db()


def add_admin():
    Admin.create(user_name="tonghs",
                 password=hashlib.md5('tonghs').hexdigest())


def test_teacher():
    t = Teacher.get(Teacher.id == 1)
    print t.method
    print t.category

if __name__ == '__main__':
    test_teacher()
