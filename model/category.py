#!usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField
from form.category import CategoryForm


class Category(Base):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    parent = IntegerField(default=0)
    created_time = IntegerField(default=int(time.time()))

    Form = CategoryForm
