#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random
from pub_config import SMS_API_KEY
from yunpian.SmsOperator import SmsOperator
from model._base import redis, R
from form.sms import SMSForm

reload(sys)
sys.setdefaultencoding('utf-8')

R_SMS = R.SMS('%s')


class SMS(object):
    @classmethod
    def new(cls, phone):
        ''' 发送短信
            生成随机四位数，然后存到 redis 中， 10 分钟过期
        '''
        smsOperator = SmsOperator(SMS_API_KEY)
        code = random.randint(1000, 9999)
        redis.setex(R_SMS % phone, 600, code)
        text = '【一块投吧】您的验证码是{code}'.format(code=code)

        result = smsOperator.single_send({'mobile': phone, 'text': text})

        return result.content.get('code', '') == 0

    @classmethod
    def verify(cls, phone, code):
        ''' 验证短信验证码
            验证成功后在 redis 中删除 key
        '''
        result = False
        if code:
            key = R_SMS % phone
            result = code == redis.get(key)
            if result:
                redis.delete(key)

        return result

    Form = SMSForm
