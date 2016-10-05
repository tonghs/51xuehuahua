#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField, TextField

from form.teacher import TeacherForm


class Teacher(Base):
    id = PrimaryKeyField()
    name = CharField()
    avatar = CharField()
    desc = TextField(default=1)
    created_time = IntegerField(default=int(time.time()))

    Form = TeacherForm
