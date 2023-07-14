# -*- coding: utf-8 -*-
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"*"})  # 允许所有来源的请求


def main(data):
    """
    对前端传入的数据进行处理

    : param data:
    : return: json_data
    """
    point, number = data["point"], data["number"]  # 解包前端传入后端的数据字典, 获取所需数据并创建实例
    name = ["number" + str(i) for i in number]  # 对前端传入后端的point, number数据进行操作
    json_data = dict(zip(name, point))  # 将处理后的数据打包成字典格式
    return json_data  # main函数的返回值


@app.route("/mesh", methods=['GET', 'Post'])  # 装饰器, 继承app.route()函数从 http://192.168.2.132:5001/mesh 获取的数据
def fetch_data():
    data = request.json  # 从前端接受数据
    return main(data)  # 将经过后端main(data)函数处理的数据以json格式返回前端


if __name__ == "__main__":
    # host: 本机的IPv4地址
    # port: 自定义端口
    app.run(host="192.168.2.132", debug=True, port=5001)
