#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 数据配置

# 打开数据库连接
db = MySQLdb.connect(host='localhost', user='wucan', passwd='wucan', charset='utf8')
db.select_db('land')

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取一条数据库。
# data = cursor.fetchone()
#
# print "Database version : %s " % data

# SQL 插入语句
sql = "INSERT INTO land(name,url, des) VALUES ('Mac', 'Mohan', 'descc')"
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    print "succ"
except Exception as e:
    # time.sleep(30)
    print type(e), e
    # Rollback in case there is any error
    db.rollback()
# 关闭数据库连接
db.close()
