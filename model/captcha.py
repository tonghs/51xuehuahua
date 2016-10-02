#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice
import captchaimage
from PIL import Image
from cStringIO import StringIO
from base64 import b64encode
from os.path import dirname, join

from model._base import redis, R
from uuid import uuid1

R_CAPTCHA = R.CAPTCHA("%s")


CHARSET = 'ABCEDEFJHIJKMNPQRSTUVWXYZ23456789'
FONT_PATH = join(dirname(__file__), "r.ttf")


class Captcha(object):
    @classmethod
    def captcha(cls, size_y=40):
        text = ''.join(choice(CHARSET) for i in xrange(5))
        image_data = captchaimage.create_image(FONT_PATH, 30, size_y, text)

        image = Image.frombytes("L", (len(image_data) / size_y, size_y), image_data)

        f = StringIO()
        image.save(f, "PNG")

        return text, b64encode(f.getvalue())

    @classmethod
    def new(cls):
        token, b64img = cls.captcha()
        key = str(uuid1())
        redis.setex(R_CAPTCHA % key, 600, token.lower())
        return key, token, b64img

    @classmethod
    def verify(cls, key, token):
        if token and (token.lower() == redis.get(R_CAPTCHA % key)):
            return True
        return False

    @classmethod
    def rm(cls, key):
        redis.delete(R_CAPTCHA % key)
