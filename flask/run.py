from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
import flaskr
from api.user import user
from biz import db
import config

app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(user, url_prefix='/user')
db.init_app(app)


@app.route('/')
def sqldaoru():
    c = app.config['DB_DB']
    r = flaskr.diaoyong()
    return r
    # return ''


if __name__ == '__main__':
    # db.init_app(app)
    # app.run(host=app.config['HOST'],
    #         port=app.config['PORT'],
    #         debug=app.config['DEBUG'])
    app.debug = False
    app.run()
