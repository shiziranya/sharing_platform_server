#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：user_service.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/18 21:34 
'''
from utils.singleton import Singleton
from Services.db_service import DBService
from loguru import logger
import os


img_path = "upload/image"
class UserService(metaclass=Singleton):
    def __init__(self):
        logger.info(f"UserService started")

    def onUserLogin(self,username:str,password):
        text:str = ""
        db_user = DBService().find_user_by_name(username)
        audit = db_user["audit"]
        if db_user is None:
            text = "用户未注册"
            return False,text
        db_password = db_user["password"]
        if db_password != password:
            text = "密码错误"
            return False,text
        elif not audit:
            text = "等待管理员审核"
            return False,text
        else:
            text = "登录成功"
            return True,text

    def onUserRegister(self,username:str,password:str,profile):
        db_user = DBService().find_user_by_name(username)
        if db_user is not None:
            text = "用户已存在"
            return False,text
        else:
            #profile save
            img_name = f"{username}_profile.png"
            profile_path = os.path.join(img_path,img_name)
            profile[0].save(profile_path)


            result = DBService().insert_user(username, password,profile_path)
            if result:
                text = "注册成功，等待管理员审核"
                return True,text
            text = "注册失败"
            return False,text

    def onUserUpload(self,title,content,anger,imgs,uid):
        img_names = []
        idx = 0
        for img in imgs:
            img_name = f"{title}-{idx}.png"
            path = os.path.join(img_path, img_name)
            img.save(path)
            img_names.append(img_name)
            idx = idx + 1
        names_str = ""
        for name in img_names:
            names_str += name
            names_str += "/"
        names_str = names_str[:-1]
        result = DBService().insert_post(title, content, 0, anger, names_str, uid)
        if result:
            text = "分享上传成功"
            return True,text
        text = "分享上传失败"
        return False,text

    def onUserComment(self,uid,angry,content,post_id):
        result = DBService().insert_comment(uid,angry,content,post_id)
        if result:
            text = "评论上传成功"
            return True,text
        text = "评论上传失败"
        return False,text

    def onUserLike(self,uid,post_id):
        result = DBService().insert_like(uid,post_id)
        if result:
            text = "点赞成功"
            return True,text
        text = "点赞失败"
        return False,text





