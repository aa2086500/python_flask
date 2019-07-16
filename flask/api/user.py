# coding:utf-8
# user
from flask import Blueprint, request
import flaskr
import json
from appcode.Encrypt import prpcrypt
user = Blueprint('user', __name__)


@user.route('/index')
def index():
    id = request.args.getlist('id')
    # r = flaskr.diaoyong()
    r = flaskr.User.query.filter(flaskr.User.id == id).first()
    return str(r)


@user.route('/lgoin', methods=['POST', 'GET'])
def lgoin():
    json_data = request.json
    account=json_data.get("username")
    paw=json_data.get("password")
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
