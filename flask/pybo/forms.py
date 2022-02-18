from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목은 필수 항목입니다.')])
    content = TextAreaField('내용', validators=[])

class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수 항목입니다.')])
    
class UserCreateForm(FlaskForm):
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    username = StringField('사용자이름')
    password1 = PasswordField('암호', validators=[DataRequired(), Length(min=6), EqualTo('password2', '암호가 일치하지 않습니다.')])
    password2 = PasswordField('암호확인', validators=[DataRequired()])

class UserLoginForm(FlaskForm):
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('암호', validators=[DataRequired()])