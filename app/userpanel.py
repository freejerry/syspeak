import uuid
from flask import Blueprint, jsonify
from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .userModel import User
from .projectModel import Project
from .chartModel import Chart, Series, Trace, Data
from . import db

bp = Blueprint('userpanel', __name__)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter(
            User.account == request.form.get('username')).first()
        if user:
            if check_password_hash(user.password, request.form.get('password')):
                login_user(user)
                # url_for(index.index) => 尋找index中index對應的路徑
                return redirect(url_for('userpanel.userpanel'))
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')
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
    project = Project.query.filter_by(
        creator=current_user.user_id, prj_id=prj_id).first()
    if request.method == 'POST':  # 填完表單進入這裡
        if request.form.get('action') == 'update':
            project.name = request.form.get(
                'prj_name')  # 將表單新填的name存入project裡的name
            project.description = request.form.get('prj_desc')
            db.session.commit()  # 下這個指令才有改資料庫的東西
        elif request.form.get('action') == 'create_chart':
            # 將表單傳入的資料存入資料庫
            chart = Chart(
                title=request.form.get('chart_title'),
                description=request.form.get('chart_description'),
                chart_type=request.form.get('chart_type'),
                x_label=request.form.get('chart_x_label'),
                y_label=request.form.get('chart_y_label'),
                project=prj_id
            )
            db.session.add(chart)
            db.session.commit()
        elif request.form.get('action') == 'create_series':
            series = Series(
                label=request.form.get('label'),
                project=prj_id
            )
            db.session.add(series)
            db.session.commit()
        elif request.form.get('action') == 'create_trace':
            trace = Trace(
                title=request.form.get('traceName'),
                chart=request.form.get('chart'),
                x_axis=request.form.get('xAxis'),
                y_axis=request.form.get('yAxis')
            )
            db.session.add(trace)
            db.session.commit()
        return redirect(url_for('userpanel.project', prj_id=prj_id))
    else:
        charts = Chart.query.filter_by(project=prj_id)
        series = Series.query.filter_by(project=prj_id)
        # 渲染樣板就是將資料庫拿到的資料，或者後端運算後的結果填進去前端的空裡面，就可以在前端看到
        return render_template('project.html', project=project, charts=charts, series=series)


@bp.route('/project/<prj_id>/delete')
@login_required
def delete(prj_id):
    project = Project.query.filter_by(
        creator=current_user.user_id, prj_id=prj_id).first()
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('userpanel.userpanel'))


@bp.route('/project/<prj_id>/chart/<chart_id>', methods=['GET', 'POST'])
@login_required
def chart(prj_id, chart_id):
    chart = Chart.query.filter_by(chart_id=chart_id).first()
    if request.method == 'POST':
        chart.title = request.form.get('chart_title')
        chart.description = request.form.get('chart_description')
        chart.x_label = request.form.get('chart_x_label')
        chart.y_label = request.form.get('chart_y_label')
        db.session.commit()
    # 過濾條件chart得id,在trace得資料庫chartid記在chart得變數裡
    traces = Trace.query.filter_by(chart=chart_id)
    series = Series.query.filter_by(project=prj_id)
    return render_template('chart.html', chart=chart, traces=traces, series=series, project=prj_id)


@bp.route('/project/<prj_id>/series/<series_id>/empty')
@login_required
def series_empty(prj_id, series_id):
    data = Data.query.filter_by(project=prj_id, series=series_id).all()
    for d in data:
        db.session.delete(d)
    db.session.commit()
    return "1"


@bp.route('/project/<prj_id>/series/<series_id>/delete')
@login_required
def series_delete(prj_id, series_id):
    trace = Trace.query.filter(
        db.or_(
            Trace.x_axis == series_id,
            Trace.y_axis == series_id
        )
    )
    if trace.count():
        return "0"
    else:
        series = Series.query.filter_by(
            project=prj_id, series_id=series_id).first()
        db.session.delete(series)
        data = Data.query.filter_by(project=prj_id, series=series_id).all()
        for d in data:
            db.session.delete(d)
        db.session.commit()
        return "1"


@bp.route('/project/<prj_id>/trace/<trace_id>/delete')
@login_required
def trace_delete(prj_id, trace_id):
    trace = Trace.query.filter_by(trace_id=trace_id).first()
    db.session.delete(trace)
    db.session.commit()
    return "1"


@bp.route('/project/<prj_id>/chart/<chart_id>/delete')
@login_required
def chart_delete(prj_id, chart_id):
    chart = Chart.query.filter_by(chart_id=chart_id).first()
    db.session.delete(chart)
    trace = Trace.query.filter_by(chart=chart_id).all()
    for t in trace:
        db.session.delete(t)
    db.session.commit()
    return redirect(url_for('userpanel.project', prj_id=prj_id))
