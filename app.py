from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from datetime import datetime


# Init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#referencing SQLAlchemcy
db = SQLAlchemy(app)

#referencing marshmallow
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    due_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    status = db.Column(db.Enum('incomplete', 'inprogress', 'completed', name='varchar'))

    def __init__(self, title, description, due_date, status):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

# TASK Schema
class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'due_date', 'status')

# Init Schema
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)

