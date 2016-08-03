from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):  # 定义登陆表单的属性，方便之后在路由器调用，它具备Form共有的属性
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])  # Email()是验证函数，必须是emai格式才行
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')