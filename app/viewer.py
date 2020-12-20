from flask import Blueprint, render_template

from .projectModel import Project
from . import db

bp = Blueprint('viewer', __name__)

@bp.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)