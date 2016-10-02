#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField


class Admin(Base):
    id = PrimaryKeyField()
    name = CharField()
    user_name = CharField(unique=True)
    pass_word = CharField()
    created_time = IntegerField(default=int(time.time()))
