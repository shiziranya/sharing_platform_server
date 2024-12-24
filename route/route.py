#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：route.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/21 19:18 
'''
from Services.user_service import UserService


from flask import Blueprint, request, jsonify
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)
SECRET_KEY = "your_secret_key"

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    result ,text = UserService().onUserRegister(username,password)
    print(text)


@auth_bp.route('/register', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    result, text = UserService().onUserLogin(username, password)
    print(text)
