from biz import db
from datetime import datetime
import time
from biz.sys_Enum import Enum_Delete, Enum_State


# 公共类
class sys_Total():
    id = db.Column(db.Integer, primary_key=True)
    sys_AddTime = db.Column(db.Date, default=datetime.now)
    sys_EndTime = db.Column(db.Date, default=datetime.now)
    sys_Delete = db.Column(db.Enum(Enum_Delete), default=Enum_Delete.未删除)
    sys_State = db.Column(db.Enum(Enum_State), default=Enum_State.可用)
    sys_Timestamp = db.Column(db.BigInteger, default=int(time.time()))
    sys_Remarks = db.Column(db.Text, default='')
    sys_Remarks1 = db.Column(db.Text, default='')
    sys_Remarks2 = db.Column(db.Text, default='')
