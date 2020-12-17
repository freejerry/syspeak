import uuid
from flask import Blueprint
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .userModel import User
from .projectModel import Project
from . import db

bp = Blueprint('userpanel', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter(User.account == request.form.get('username'),
                                 User.password == request.form['password']).first()
        if user:
            login_user(user)
            # url_for(index.index) => 尋找index中index對應的路徑
            return redirect(url_for('userpanel.userpanel'))
    else:
        return render_template('login.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('userpanel.login'))


@bp.route('/')
@login_required  # 有這個才會導到login頁面，別人寫好的，直接拿來用
def userpanel():
    projects = Project.query.filter_by(creator=current_user.user_id)  # 查詢資料庫
    # 沒有login required直接return 這個
    return render_template('userpanel.html', projects=projects)


@bp.route('/new_project', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        api_key = str(uuid.uuid4())
        creator = current_user.user_id
        project = Project(  # 建資料
            name=request.form.get('prj_name'),
            description=request.form.get('prj_desc'),
            api_key=api_key,
            creator=creator
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('userpanel.userpanel'))
    else:
        return "看三小"


@bp.route('/project/<prj_id>', methods=['GET', 'POST'])
@login_required
def project(prj_id):
    project = Project.query.filter_by(creator=current_user.user_id, prj_id=prj_id).first()
    if request.method == 'POST':  # 填完表單進入這裡
        project.name = request.form.get('prj_name')  # 將表單新填的name存入project裡的name
        project.description = request.form.get('prj_desc')
        db.session.commit()  # 下這個指令才有改資料庫的東西
        return redirect(url_for('userpanel.project', prj_id=prj_id))
    else:
        return render_template('project.html', project=project)  # 一開始進入到這裡

@bp.route('/project/<prj_id>/delete')
@login_required
def delete(prj_id):
    project = Project.query.filter_by(creator=current_user.user_id, prj_id=prj_id).first()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('userpanel.userpanel'))