from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class TrainingDataModel(db.Model):
    __tablename__ = 'training_table'

    id = db.Column(db.Integer, primary_key=True)
    ans = db.Column(db.Integer)
    dataURL = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return TrainingDataModel.query.order_by(TrainingDataModel.id).all()

def insert(ans, data):
    model = TrainingDataModel(ans=ans, dataURL=data)
    db.session.add(model)
    db.session.commit()