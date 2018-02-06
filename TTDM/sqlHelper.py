#-*- coding: utf-8 -*-
#***********************************************
#
#      Filename: sqlHelper.py
#
#        Author: Benson - zjxucb@gmail.com
#   Description: ---
#        Create: 2018-02-05 15:39:24
# Last Modified: 2018-02-06 09:17:58
#***********************************************

import pymysql

class sqlHelper(object):
    """docstring for sqlHelper."""
    def __init__(self, arg):
        super(sqlHelper, self).__init__()
        self.arg = arg

    #创建数据库表
    def Create_database_table(arg):
        print("Create_database_table!")
        # 打开数据库连接
        db = pymysql.connect("localhost","root","","labels" )
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        # 使用预处理语句创建表
        sql = """CREATE TABLE EMPLOYEE (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,
                 SEX CHAR(1),
                 INCOME FLOAT )"""
        cursor.execute(sql)
        # 关闭数据库连接
        db.close()

    #数据库插入操作
    def Insert_Database(arg):
        print("Insert_Database!")
        # 打开数据库连接
        db = pymysql.connect("localhost","root","","labels" )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
                 LAST_NAME, AGE, SEX, INCOME)
                 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 如果发生错误则回滚
           db.rollback()
        # 关闭数据库连接
        db.close()

    #数据库查询操作
    def Query_Database(arg):
        # 打开数据库连接
        db = pymysql.connect("localhost","root","","labels" )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM EMPLOYEE \
                WHERE INCOME > '%d'" % (1000)
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                fname = row[0]
                lname = row[1]
                age = row[2]
                sex = row[3]
                income = row[4]
                # 打印结果
                print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                (fname, lname, age, sex, income ))
        except:
            print ("Error: unable to fetch data")
            # 关闭数据库连接
            db.close()
    #数据库更新操作
    def Updata_Database(arg):
        # 打开数据库连接
        db = pymysql.connect("localhost","root","","labels" )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 更新语句
        sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 发生错误时回滚
           db.rollback()
        # 关闭数据库连接
        db.close()

    #删除操作
    def Del_Database(arg):
        # 打开数据库连接
        db = pymysql.connect("localhost","root","","labels" )
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 删除语句
        sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 提交修改
           db.commit()
        except:
           # 发生错误时回滚
           db.rollback()
        # 关闭连接
        db.close()



print ("sqlHelper test ^_^ ")
dd = sqlHelper("Create")
dd.Create_database_table()
dd.Insert_Database()
dd.Query_Database()
dd.Updata_Database()
dd.Del_Database()
