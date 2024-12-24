#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：singleton.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/18 21:38 
'''
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]