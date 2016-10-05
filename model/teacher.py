#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField, TextField

from form.teacher import TeacherForm


class TeacherMethod(Base):
    teacher_id = IntegerField()
    method_id = IntegerField()

    class Meta:
        db_table = 'teacher_method'


class TeacherCategory(Base):
    teacher_id = IntegerField()
    category_id = IntegerField()

    class Meta:
        db_table = 'teacher_category'


class Teacher(Base):
    id = PrimaryKeyField()
    name = CharField()
    avatar = CharField()
    desc = TextField(default=1)
    created_time = IntegerField(default=int(time.time()))

    Form = TeacherForm

    def set_method(self, method_list):
        for method in map(int, method_list):
            TeacherMethod.create(teacher_id=self.id,
                                 method_id=method)

    def set_category(self, category_list):
        for category in map(int, category_list):
            TeacherCategory.create(teacher_id=self.id,
                                   category_id=category)
