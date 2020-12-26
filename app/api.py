from flask import Blueprint, request, jsonify

from .projectModel import Project
from .chartModel import Series, Data, Chart, Trace
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
                data=d,
                series=ser,
                project=prj_id,
            )
            db.session.add(data)
            db.session.commit()
    return "1"

@bp.route('/getchart/<prj_id>/<mode>')
def getchart(prj_id, mode):
    if(mode == 'all'):
        #project = Project.query.filter_by(prj_id=prj_id).first()
        data = []
        charts = Chart.query.filter_by(project = prj_id).all()
        for chart in charts:
            t_data = []
            traces = Trace.query.filter_by(chart = chart.chart_id).all()
            for trace in traces:
                if chart.chart_type == 0:
                    t = {
                        'title': trace.title,
                        'x_axis': trace.x_axis,
                        'y_axis': trace.y_axis
                    }
                elif chart.chart_type == 9:
                    t = {
                        'title': trace.title,
                        'series': trace.x_axis
                    }
                t_data.append(t)
            c = {
                'id': chart.chart_id,
                'title': chart.title,
                'description': chart.description,
                'chart_type': chart.chart_type,
                'x_label': chart.x_label,
                'y_label': chart.y_label,
                'traces' : t_data
            }
            data.append(c)
        return jsonify(data)

@bp.route('/getseries/<prj_id>/<mode>')
def getseries(prj_id, mode):
    if(mode == 'top1000'):
        series = Series.query.filter_by(project = prj_id).all() #取出選定project的全部series
        data = {} #設定data為一個陣列
        for ser in series: # 將取出的所有series用for分離
            d = Data.query.filter_by(series = ser.series_id).limit(1000).all() # 取出特定series裡的前1000筆最新資料
            data[ser.series_id] = [dd.serialize for dd in d] #data取出是一個structure，太多筆不能被serialize，所以在用一個for分離
        return jsonify(data)
    return {0}
'''
@bp.route('/empty', methods=['POST'])
def empty():
    json = request.get_json()
    project = Project.query.filter_by(api_key=json['api_key']).first()
    prj_id = project.prj_id
    
    return str(project.prj_id)
'''