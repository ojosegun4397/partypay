from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()





      
class User(db.Model):  
    user_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_fullname = db.Column(db.String(100),nullable=False)
    user_email = db.Column(db.String(120)) 
    
  
    
class Donation(db.Model):
    don_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    don_amt = db.Column(db.Float, nullable=False)  
    don_userid = db.Column(db.Integer,db.ForeignKey("user.user_id"),nullable=True)
    don_fullname = db.Column(db.String(100),nullable=True)
    don_email = db.Column(db.String(100),nullable=True)

    don_refno=db.Column(db.String(20), nullable=False)
    don_paygate_response=db.Column(db.Text())

    don_date = db.Column(db.DateTime(), default=datetime.utcnow)
    don_status =db.Column(db.Enum('pending','failed','paid'),nullable=False, server_default=("pending"))  
    #set relationship
    donor = db.relationship('User',backref='mydonations')

