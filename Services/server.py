#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：server.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/21 17:07 
'''
from utils.singleton import Singleton
from Services.db_service import DBService
from Services.user_service import UserService


class Server(metaclass=Singleton):
    def __init__(self):
        self.dbService = DBService()
        self.userService = UserService()

