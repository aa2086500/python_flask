from db.sys_Total import sys_Total
from run import db
# 用户表管理
class T_User(db.Model,sys_Total):
  __tablename__ = "T_User"
  name = db.Column(db.String(32),unique=True)
  name = db.Column(db.String(32),unique=True)
  # 相当于__str__方法。
  def __repr__(self):
    return "Role: %s %s" % (self.id,self.name)
