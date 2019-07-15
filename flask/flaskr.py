# -*- coding:utf-8 -*-
from biz import db
import biz.sys.t_User


class Role(db.Model):

    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 给Role类创建一个uses属性，关联users表。
    # backref是反向的给User类创建一个role属性，关联roles表。这是flask特殊的属性。
    users = db.relationship('User', backref="role")

    # 相当于__str__方法。
    def __repr__(self):
        return "Role: %s %s" % (self.id, self.name)


class User(db.Model):
    # 给表重新定义一个名称，默认名称是类名的小写，比如该类默认的表名是user。
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(16))
    # 创建一个外键，和django不一样。flask需要指定具体的字段创建外键，不能根据类名创建外键
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return "User: %s %s %s %s" % (self.id, self.name, self.password,
                                      self.role_id)


def hello_world():
    return 'Hello World!'


def diaoyong():
    # r=User.query.all()
    # return r
    # 删除所有的表
    db.drop_all()
    # 创建表
    db.create_all()
    ro1 = Role(name="admin")
    # 先将ro1对象添加到会话中，可以回滚。
    db.session.add(ro1)
    ro2 = Role()
    ro2.name = 'user'
    db.session.add(ro2)
    # 最后插入完数据一定要提交
    db.session.commit()
    us1 = User(name='wang',
               email='wang@163.com',
               password='123456',
               role_id=ro1.id)
    us2 = User(name='zhang',
               email='zhang@189.com',
               password='201512',
               role_id=ro2.id)
    us3 = User(name='chen',
               email='chen@126.com',
               password='987654',
               role_id=ro2.id)
    us4 = User(name='zhou',
               email='zhou@163.com',
               password='456789',
               role_id=ro1.id)
    us5 = User(name='tang',
               email='tang@itheima.com',
               password='158104',
               role_id=ro2.id)
    us6 = User(name='wu',
               email='wu@gmail.com',
               password='5623514',
               role_id=ro2.id)
    us7 = User(name='qian',
               email='qian@gmail.com',
               password='1543567',
               role_id=ro1.id)
    us8 = User(name='liu',
               email='liu@itheima.com',
               password='867322',
               role_id=ro1.id)
    us9 = User(name='li',
               email='li@163.com',
               password='4526342',
               role_id=ro2.id)
    us10 = User(name='sun',
                email='sun@163.com',
                password='235523',
                role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()
