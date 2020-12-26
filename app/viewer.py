from flask import Blueprint, render_template

from .projectModel import Project
from .chartModel import Chart
from . import db

bp = Blueprint('viewer', __name__)

@bp.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

@bp.route('/project/<prj_id>')
def project(prj_id):
    project = Project.query.filter_by(prj_id = prj_id).first()
    charts = Chart.query.filter_by(project = prj_id)
    return render_template('view.html', project=project, charts=charts)