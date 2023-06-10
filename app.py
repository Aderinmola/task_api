from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from datetime import datetime
from flask_migrate import Migrate


# Init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#referencing SQLAlchemcy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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

# Create a Task
@app.route('/task', methods=['POST'])
def add_task():
    default_date = "2023-06-03T15:11:16"

    title = request.json['title']
    description = request.json['description']
    due_date = datetime.fromisoformat(request.json.get('due_date', default_date))
    status = request.json['status']

    if status not in ['incomplete', 'inprogress', 'completed']:
        return "Task status is not valid!!!"

    new_task = Task(title, description, due_date, status)
    if Task.query.filter_by(title=title).count() == 0:
        db.session.add(new_task)
        db.session.commit()
        return task_schema.jsonify(new_task)
    else:
        return "Task already exist!!!"


# Get All Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():

    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    all_tasks = Task.query.paginate(page=page, per_page=per_page)

    meta={
        "page": all_tasks.page,
        "pages": all_tasks.pages,
        "total_count": all_tasks.total,
        "prev_page": all_tasks.prev_num,
        "next_page": all_tasks.next_num,
        "has_next": all_tasks.has_next,
        "has_prev": all_tasks.has_prev,
    }
    result = tasks_schema.dump(all_tasks)

    return jsonify({'data': result, 'meta': meta})

#get a particular task
@app.route('/task/<id>', methods=['GET'])
def singleTask(id):
    single_task = Task.query.get(id)
    if single_task != None:
        return task_schema.jsonify(single_task)
    else:
        return "Task does not exist!!!"
    
# Update a Task
@app.route('/task/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    default_date = "2023-06-03T15:11:16"


    if task != None:
        title = request.json['title']
        description = request.json['description']
        due_date = datetime.fromisoformat(request.json.get('due_date', default_date))
        status = request.json['status']

        task.title = title
        task.description = description
        task.due_date = due_date
        task.status = status

        db.session.commit()
        return task_schema.jsonify(task)
    else:
        return "Task does not exist!!!"
    
# Delete Task
@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if task != None:
        db.session.delete(task)
        db.session.commit()
        return task_schema.jsonify(task)
    else:
        return "Task does not exist!!!"

if __name__ == '__main__':
    app.run(debug=True)
