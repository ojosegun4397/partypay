from flask import Flask
from flask_migrate import Migrate #new addition
from flask_wtf.csrf import CSRFProtect
csrf=CSRFProtect()



def createapp():
    app=Flask(__name__)
    from party import config
    app.config.from_pyfile('config.py', silent=True)
    from party.models import db
    db.init_app(app)
    csrf.init_app(app)
    migrate=Migrate(app,db) #NEW ADDITION
    return app


app=createapp()

from party import userroute,forms,models