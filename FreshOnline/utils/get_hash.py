#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from hashlib import sha1


# 编写加密的get_hash函数
def get_hash(str, salt=None):
    '''
    获取一个字符串的hash值
    '''
    # 在工作中，为了加大密码的破解难度，可以把传进来的字符串再次进行混淆
    # 也可以再指定一个值salt, 拼接到字符串中，再次添加混淆
    str = '!@#$%' + str + '%$#@!'
    if salt:
        str = str + salt

    sh = sha1()
    sh.update(str.encode('utf-8'))
    return sh.hexdigest()