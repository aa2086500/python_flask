from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setAttr(self, e, prop):
    a=e.get(prop)
    if a:
        # if type(a)==list:
        #     a=str(a)
        self.__setattr__(prop, a)
db.Model.setAttr=setAttr