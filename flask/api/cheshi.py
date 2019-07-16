# coding:utf-8
# user
from flask import Blueprint, request
import flaskr
import json
from appcode.Encrypt import prpcrypt
user = Blueprint('user', __name__)

@user.route('/add12')
def add():
    return 'user_add'


@user.route('/show2')
def show():
    return 'user_show'
