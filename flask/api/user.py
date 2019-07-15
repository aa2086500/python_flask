#coding:utf-8
#user
from flask import Blueprint,request
import flaskr
user = Blueprint('user', __name__)


@user.route('/index')
def index():
    id = request.args.getlist('id')
    # r = flaskr.diaoyong()
    r = flaskr.User.query.filter(flaskr.User.id==id).first()
    return str(r)


@user.route('/add')
def add():
    return 'user_add'


@user.route('/show')
def show():
    return 'user_show'