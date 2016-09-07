#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField, TimeField

from form.user import UserForm


class User(Base):
    id = PrimaryKeyField()
    name = CharField()
    phone = CharField(unique=True)
    email = CharField(unique=True)
    gender = IntegerField(default=1)
    avatar = CharField()
    birthday = TimeField()
    creation_time = IntegerField(default=int(time.time()))

    Form = UserForm
