#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Sharing_Platform_Server 
@File    ：db_manager.py
@IDE     ：PyCharm 
@Author  ：Ran
@Date    ：2024/12/18 21:33 
'''
from utils.singleton import Singleton
import pymysql
from pymysql.cursors import DictCursor
from loguru import logger


class DBManager(metaclass=Singleton):
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "0000"
        self.database = "sharing_platform_db"
        self.port = 3306
        self.connection = None

    def connect(self):
        """
        创建数据库连接
        """
        try:
            self.connection = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                cursorclass=DictCursor  # 使用字典游标，可以将结果作为字典返回
            )
            logger.info("DBManager started")
        except pymysql.MySQLError as e:
            print(f"数据库连接失败: {e}")
            raise

    def execute_query(self, query, params=None):
        """
        执行查询
        :param query: SQL 查询语句
        :param params: 可选的SQL查询参数
        :return: 查询结果
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        except pymysql.MySQLError as e:
            print(f"查询执行失败: {e}")
            raise

    def execute_update(self, query, params=None):
        """
        执行更新或插入操作
        :param query: SQL语句
        :param params: 可选的SQL参数
        :return: 受影响的行数
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.connection.commit()
                return cursor.rowcount
        except pymysql.MySQLError as e:
            print(f"更新或插入操作失败: {e}")
            self.connection.rollback()
            raise