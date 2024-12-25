#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/21 19:24 
'''
from flask import Flask
from flasgger import Swagger
from Services.server import Server
from route.user import user
from route.admin import admin


server = Server()


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "upload/image"
app.register_blueprint(user)
app.register_blueprint(admin)
swagger = Swagger(app)

if __name__ =="__main__":
    app.run()

