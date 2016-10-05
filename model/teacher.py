#!/usr/bin/env python
# -*- coding: utf-8 -*-

import _env  # noqa
import time
from model._base import Base
from peewee import CharField, IntegerField, PrimaryKeyField, TextField

from form.teacher import TeacherForm
from model.teach_method import TEACH_METHOD_CN
from model.category import Category
from pub_config import QINIU


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

    @property
    def method(self):
        li = TeacherMethod.select().where(TeacherMethod.teacher_id == self.id)

        return [TEACH_METHOD_CN.get(o.method_id) for o in li]

    @property
    def category(self):
        li = TeacherCategory.select().where(TeacherCategory.teacher_id == self.id)
        category_id_list = [o.category_id for o in li]
        category_li = Category.select().where(Category.id << category_id_list)

        return [o.name for o in category_li]

    @property
    def avatar_(self):
        return '{qiniu_host}{key}'.format(qiniu_host=QINIU.HOST, key=self.avatar)

    @classmethod
    def list(cls, page=1, limit=15):
        count = cls.select().count()
        page = 1 if page < 1 else page
        total_page = 0

        total_page, mod = divmod(count, limit)
        total_page = total_page + 1 if mod else total_page

        if page > total_page:
            page = total_page

        return cls.select().order_by(cls.created_time.desc()).paginate(page, limit), count, total_page
