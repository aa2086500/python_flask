DB_USER = 'root'
DB_PASSWORD = 'cgf123456'
DB_HOST = 'localhost:3306'
DB_DB = 'flaskr'

DEBUG = True
PORT = 5000
HOST = "127.0.0.1"
SECRET_KEY = "my blog"

SQLALCHEMY_TRACK_MODIFICATIONS = False
# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://用户名：密码@ip地址：端口号/flaskr?charset=utf8'
SQLALCHEMY_DATABASE_URI = 'mysql://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_DB+'?charset=utf8'