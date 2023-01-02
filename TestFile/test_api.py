import flask
import json
from flask import request

server = flask.Flask(__name__)


@server.route('/login',methods=['get','post'])


def login():
    username = request.values.get('name')

    pwd = request.values.get('pwd')

    if username and pwd:
        if username == "xiaoming" and pwd == "123456":
            res = {"code":200,'msg':"登录成功！"}
            return json.dumps(res,ensure_ascii=False)   # 将字典转换为字符串
        else:
            res = {"code":203,'msg':"账号或密码错误"}
            return json.dumps(res,ensure_ascii=False)
    else:
        res = {"code":204,'msg':"账号或密码不能为空！"}
        return json.dumps(res,ensure_ascii=False)

if __name__ == "__main__":
    server.run(debug=True,port=8888,host="127.0.0.1")

