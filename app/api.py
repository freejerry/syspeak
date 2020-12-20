from flask import Blueprint, request

from .projectModel import Project
from .chartModel import Series, Data
from . import db

bp = Blueprint('api', __name__)

@bp.route('/insertdata', methods=['POST'])
def insertdata():
    json = request.get_json()
    project = Project.query.filter_by(api_key=json['api_key']).first()
    prj_id = project.prj_id
    for ser, d in json['data'].items():
        series = Series.query.filter_by(series_id=ser, project=prj_id)
        if series.count():
            data = Data(
                data = d,
                series = ser,
                project = prj_id,
            )
            db.session.add(data)
            db.session.commit()
    return str(project.prj_id)

@bp.route('/empty', methods=['POST'])
def empty():
    json = request.get_json()
    project = Project.query.filter_by(api_key=json['api_key']).first()
    prj_id = project.prj_id
    
    return str(project.prj_id)