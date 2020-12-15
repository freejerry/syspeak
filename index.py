from flask import Blueprint#從flask引入藍圖的功能
from flask import render_template

bp = Blueprint('index', __name__)# 藍圖名字叫index並存成index變數

@bp.route('/')  #  路由上標名了生產
def index():
    return render_template('index.html')