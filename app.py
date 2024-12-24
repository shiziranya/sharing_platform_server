#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：app.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/21 19:24 
'''
from flask import Flask,Blueprint, request, jsonify,send_from_directory,render_template
from flasgger import Swagger
from route.route import auth_bp
from Services.user_service import UserService
from Services.server import Server
from Services.db_service import DBService
import os


server = Server()


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "upload/image"
swagger = Swagger(app)


@app.route('/user/register', methods=['POST'])
def register():
    """

    :return:
    """
    data = request.form
    username = data.get("username")
    password = data.get("password")
    imgs = request.files.getlist("profile")
    result,text = UserService().onUserRegister(username,password,imgs)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)



@app.route('/user/login', methods=['POST'])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    result, text = UserService().onUserLogin(username, password)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)

@app.route('/user/upload', methods=['POST'])
def upload_post():
    data = request.form
    title = data.get("title")
    content = data.get("content")
    anger = int(data.get("anger"))
    uid = data.get("uid")
    imgs = request.files.getlist("file_imgs")

    img_paths = UserService().onUserUpload(title,content,anger,imgs,uid)
    response = {
        "code":200,
        "message":"分享上传成功"
    }
    return jsonify(response)

@app.route("/user/comment",methods=['POST'])
def upload_comment():
    data = request.form
    uid = data.get("uid")
    angry = data.get("angry")
    content = data.get("content")
    post_id = data.get("post_id")
    result, text = UserService().onUserComment(uid,angry,content,post_id)
    if result:
        response = {
            "code":200,
            "message":text
        }
    else:
        response = {
            "code": 500,
            "message": text
        }
    return jsonify(response)

@app.route("/get_all_post", methods=['GET'])
def get_all_post():
    posts = DBService().get_posts()
    response = {
        "code": 200,
        "message": posts
    }
    return jsonify(response)

@app.route("/get_user_post/<id>", methods=['GET'])
def get_user_post(id):
    posts = DBService().get_user_post(id)
    response = {
        "code": 200,
        "message": posts
    }
    return jsonify(response)


@app.route("/get_user/<id>",methods = ["GET"])
def get_user(id):
    user = DBService().get_user(id)
    if user is not None:
        return jsonify({"code":200,"message":user})
    else:
        return jsonify({"code":500,"message":"用户id不存在"})


#图片链接接口
@app.route("/upload/image/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)



app.run()
