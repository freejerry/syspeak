from . import db

class Chart(db.Model):
    __tablename__ = 'chart'

    chart_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20))
    description = db.Column(db.String(60))
    chart_type = db.Column(db.Integer)
    x_label = db.Column(db.String(20))
    y_label = db.Column(db.String(20))
    project = db.Column(db.Integer)

    def __init__(self, chart_id=None, title=None, description=None, chart_type=None, x_label=None, y_label=None, project=None):
        self.chart_id = chart_id
        self.title = title
        self.description = description
        self.chart_type = chart_type
        self.x_label = x_label
        self.y_label = y_label
        self.project = project

    def type_text(self):
        type_name = {0: "Line graph", 9: "Heatmap"}
        return type_name[self.chart_type]

    def __repr__(self):
        return '<Project %r>' % self.title

    def __str__(self):
        return '<Project %s>' % self.title

    def serialize(self):
        return {"chart_id": self.chart_id,
                "title": self.title,
                "description": self.description,
                "chart_type": self.chart_type,
                "x_label": self.x_label,
                "y_label": self.y_label,
                "project": self.project}

class Series(db.Model):
    __tablename__ = 'series'

    series_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(20))
    project = db.Column(db.Integer)

    def __init__(self, series_id=None, label=None, project=None):
        self.series_id = series_id
        self.label = label
        self.project = project

    def __repr__(self):
        return '<Project %r>' % self.title

    def __str__(self):
        return '<Project %s>' % self.title

class Trace(db.Model):
    __tablename__ = 'trace'

    trace_id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(20))
    chart = db.Column(db.Integer)
    x_axis = db.Column(db.Integer)
    y_axis = db.Column(db.Integer)

    def __init__(self, trace_id=None, title=None, chart=None, x_axis=None, y_axis=None):
        self.trace_id = trace_id
        self.title = title
        self.chart = chart
        self.x_axis = x_axis
        self.y_axis = y_axis

    def __repr__(self):
        return '<Project %r>' % self.title

    def __str__(self):
        return '<Project %s>' % self.title