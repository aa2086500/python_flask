from biz.sys_Total import sys_Total
from biz import db
# 用户表管理
class T_User(db.Model,sys_Total):
  __tablename__ = "T_User"
  name = db.Column(db.String(32),default='')
  photo = db.Column(db.String(32),default='')
  account = db.Column(db.String(32),default='')
  password = db.Column(db.String(32),default='')
  permissionsid = db.Column(db.String(32),default='')
  # 相当于__str__方法。
  def __repr__(self):
    return "Role: %s %s" % (self.id,self.name)
