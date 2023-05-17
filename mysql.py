import os

import pymysql
from dotenv import load_dotenv
load_dotenv()

def create_connection():
    connection = pymysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),  # 用你的MySQL用户名替换
        password=os.getenv('MYSQL_PASSWORD'),  # 用你的MySQL密码替换
        database=os.getenv('MYSQL_DATABASE')
    )
    return connection


def get_table_structure():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'employees'
    """)
    result = cursor.fetchall()
    connection.close()
    # 将元组列表转换为字典列表
    columns = [
        {
            "table_name": column[0],
            "column_name": column[1],
            "data_type": column[2]
        }
        for column in result
    ]
    return columns


def execute_query(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.close()

    # 将结果封装在一个字典中
    response = {
        "result": result
    }
    return response








