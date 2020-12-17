from flask import Blueprint#從flask引入藍圖的功能
from flask import render_template

from . import login_manager
from .userModel import User

bp = Blueprint('hello', __name__)# 藍圖名字叫index並存成index變數

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/hi')  #  路由上標名了生產
def hi():
    return "hi"