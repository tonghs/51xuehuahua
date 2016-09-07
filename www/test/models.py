#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
# from model._base import drop_table, init_db
from model.user import User
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


if __name__ == '__main__':
    main()
