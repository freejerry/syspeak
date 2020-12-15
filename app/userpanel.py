from flask import Blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user
from .userModel import User

bp = Blueprint('userpanel', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter(User.account == request.form.get('username'),
                                 User.password == request.form['password']).first()
        if user:
            login_user(user)
            return redirect(url_for('index.index')) # url_for(index.index) => 尋找index中index對應的路徑
    return render_template('login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('userpanel.login'))