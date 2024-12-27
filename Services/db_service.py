#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：db_service.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/18 21:32 
'''
from Managers.db_manager import DBManager



from utils.singleton import Singleton
import pymysql
from pymysql.cursors import DictCursor
from loguru import logger

class DBService(metaclass=Singleton):
    def __init__(self):
        logger.info(f"DBServer started")
        self.db_manager = DBManager()
        self.db_manager.connect()

    def find_user_by_name(self, name:str):
        """
        根据name从users表中查找用户数据
        :param name: 用户名
        :return: 返回匹配的用户数据（如果存在），否则返回None
        """
        query = "SELECT * FROM user WHERE username = %s;"
        try:
            result = self.db_manager.execute_query(query, (name,))
            if result:
                return result[0]  # 返回匹配的第一条记录
            else:
                return None
        except Exception as e:
            print(f"查询失败: {e}")
            return None

    def insert_user(self, name:str, password:str, profile_path):
        """
        插入用户数据到users表
        :param user_id: 用户ID
        :param name: 用户名
        :param password: 用户密码
        :return: 受影响的行数
        """
        query = "INSERT INTO user (username, password, audit, profile) VALUES (%s, %s, 0, %s);"
        try:
            rows_affected = self.db_manager.execute_update(query, (name, password, profile_path))
            return rows_affected
        except Exception as e:
            print(f"插入数据失败: {e}")
            return False

    def insert_post(self,title,content,like,anger,image_path,uid):
        query = "INSERT INTO post (title,content,`like`,anger,image,uid) VALUES (%s, %s, %s, %s, %s, %s);"
        try:
            rows_affected = self.db_manager.execute_update(query,(title,content,like,anger,image_path,uid))
            return rows_affected
        except Exception as e:
            print(f"插入失败: {e}")
            return False

    def insert_comment(self,uid,angry,content,post_id):
        query = "INSERT INTO comment (uid,angry,content,post_id) VALUES (%s, %s, %s, %s);"
        try:
            rows_affected = self.db_manager.execute_update(query, (uid,angry,content,post_id))
            return rows_affected
        except Exception as e:
            print(f"插入失败: {e}")
            return False

    def insert_like(self,uid,post_id):
        query = "INSERT INTO post_like (uid,post_id) VALUES (%s, %s);"
        try:
            rows_affected = self.db_manager.execute_update(query, (uid,post_id))
            return rows_affected
        except Exception as e:
            print(f"插入失败: {e}")
            return False


    def get_posts(self):
        query = "SELECT * FROM post;"
        try:
            posts = self.db_manager.execute_query(query)
            for post in posts:
                post["image"] = post["image"].split("/")
                query = "SELECT * FROM comment WHERE post_id = %s;"
                comments = self.db_manager.execute_query(query, (post["id"]))
                query = "SELECT * FROM post_like WHERE post_id = %s;"
                likes = self.db_manager.execute_query(query, (post["id"]))
                post["comment"] = comments
                post["like"] = likes
            return posts
        except Exception as e:
            print(f"查找失败: {e}")
            return False

    def get_user_post(self,id):
        query = "SELECT * FROM post WHERE uid = id;"
        try:
            posts = self.db_manager.execute_query(query)
            for post in posts:
                post["image"] = post["image"].split("/")
                query = "SELECT * FROM comment WHERE post_id = %s;"
                result = self.db_manager.execute_query(query, (post["id"]))
                post["comment"] = result
            return posts
        except Exception as e:
            print(f"查找失败: {e}")
            return False

    def get_user(self,id):
        query = "SELECT id,username,profile FROM user WHERE id = %s;"
        try:
            result = self.db_manager.execute_query(query, (id))
            if result:
                return result  # 返回匹配的第一条记录
            else:
                return None
        except Exception as e:
            print(f"查询失败: {e}")
            return None


