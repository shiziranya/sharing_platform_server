#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/18 21:50 
'''
from Services.db_service import DBService
from Services.server import Server
server = Server()
rel = server.userService.onUserLogin("ran","1234")

print(rel)