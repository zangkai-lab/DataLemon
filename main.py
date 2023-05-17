from flask import Flask, send_from_directory,request
from flask_cors import CORS
from mysql import get_table_structure, execute_query


app = Flask(__name__)
CORS(app)


@app.get("/logo.png")
def logo():
    return send_from_directory(app.root_path, "logo.png")


@app.get("/.well-known/ai-plugin.json")
def plugin_manifest():
    with open(".well-known/ai-plugin.json") as f:
        return f.read()


@app.get("/openapi.yaml")
def openapi():
    with open("openapi.yaml") as f:
        return f.read()


@app.get("/structure")
def dataset_schema():
    return get_table_structure()


@app.route("/execute", methods=['POST'])
def sql_execute():
    request_data = request.json  # 从请求中获取JSON数据
    sql = request_data.get("sql")  # 从JSON数据中获取SQL语句
    if sql is None:  # 如果没有获取到SQL语句，返回一个错误信息
        return {"error": "No SQL provided"}
    return execute_query(sql)  # 执行SQL语句并返回结果


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1163)

