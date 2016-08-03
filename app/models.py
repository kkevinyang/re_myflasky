# from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    sqlite_autoincrement = True
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))

    @property
    def password(self):  # 若尝试读取password的值会返回属性错误，因为生成了散列值后不能还原
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):  # 生成散列值
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):  # 验证输入的散列值，对的话返回True
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


@login_manager.user_loader  # 此乃回调函数，用来加载用户，不然就会提示User没有登陆激活了（'User' object has no attribute 'is_active'）
def load_user(user_id):
    return User.query.get(int(user_id))
