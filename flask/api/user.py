# coding:utf-8
# user
from flask import Blueprint, request
import flaskr
from appcode.Encrypt import prpcrypt
user = Blueprint('user', __name__)


@user.route('/index')
def index():
    id = request.args.getlist('id')
    # r = flaskr.diaoyong()
    r = flaskr.User.query.filter(flaskr.User.id == id).first()
    return str(r)


@user.route('/lgoin/<paw>/')
def lgoin(paw):
    print(paw)
    # account = request.form.getlist('account')
    # paw = request.form.getlist('password')
    sj = prpcrypt()
    re = sj.encrypt(paw)
    return re


@user.route('/article1/<paw>/')
def jiemi(paw):
    sj = prpcrypt()
    re = sj.decrypt(paw)
    return re


@user.route('/add1')
def add():
    return 'user_add'


@user.route('/show')
def show():
    return 'user_show'
