#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
from pub_config import QINIU
import hmac
from hashlib import sha1
from base64 import urlsafe_b64encode
import json


class Token(object):
    def __init__(self, scope, key, secret, expires_in=999999):
        self._key = key
        self._secret = secret
        self._expires_in = expires_in
        self._scope = scope

    def _sign(self, kwds):
        params = dict(scope=self._scope)
        params.update(kwds)
        params['deadline'] = int(time.time()) + self._expires_in
        params['customer'] = None

        return urlsafe_b64encode(json.dumps(params))

    def _encode(self, signature):
        hashed = hmac.new(self._secret, signature, sha1)
        return urlsafe_b64encode(hashed.digest())

    def new(self, **kwds):
        signature = self._sign(kwds)
        encoded_digest = self._encode(signature)
        return '%s:%s:%s' % (self._key, encoded_digest, signature)

QINIU_TOKEN = Token(QINIU.BUCKET, QINIU.ACCESS_KEY, QINIU.SECRET_KEY)
