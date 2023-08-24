from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email,Length, EqualTo






# class Payment(FlaskForm):
#     name=StringField("Fullname",validators=[DataRequired(message="you should supply your name")])
#     phone=StringField("phone",validators=[DataRequired()])
#     email=StringField('Email', validators=[Email()])
#     message= TextAreaField("message")

#     btn=SubmitField("send message")