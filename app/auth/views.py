from flask import render_template
from . import auth
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from ..models import User
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)  # 如果传入的remember_me结果是true，则会在浏览器写入一个长期有效的cookie
            return redirect(request.args.get('next') or url_for('main.index'))  # request.args是字典
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required  # 调用的flask_login的一个方法，要求是登陆状态才行
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))