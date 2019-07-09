from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import flaskr
from api.user import user
from biz import db
app = Flask(__name__)
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:chen2086500@47.95.226.22:3306/flaskr?charset=utf8'
app.config[
    "SQLALCHEMY_DATABASE_URI"] = "mysql://root:chen2086500.@47.105.120.251:3306/flaskr?charset=utf8"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.register_blueprint(user, url_prefix='/user')

db.init_app(app)


@app.route('/')
def sqldaoru():
    # r= flaskr.diaoyong()
    # return r
    return ''


if __name__ == '__main__':
    # db.init_app(app)
    app.debug = False
    app.run()
