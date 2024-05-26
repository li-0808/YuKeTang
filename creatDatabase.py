"""
此文件用于以后使用数据库实现的方法
暂时归档


import mysql.connector

def create_classInfo():
    conn = mysql.connector.connect(
        host='',  # 数据库主机地址
        user='',  # 数据库用户名
        passwd='',  # 数据库密码
        database=''  # 数据库名
    )
    cursor = conn.cursor()

    # 检查表是否存在
    cursor.execute("SHOW TABLES LIKE 'class_info'")
    result = cursor.fetchone()
    if result:
        print("表 'class_info' 已经存在。")
    else:
        cursor.execute("CREATE TABLE IF NOT EXISTS class_info ("
                       "classroom_id INT PRIMARY KEY, "
                       "course_name VARCHAR(255), "
                       "course_sign VARCHAR(255))")
        print("已创建表 'class_info'。")

    conn.close()


"""