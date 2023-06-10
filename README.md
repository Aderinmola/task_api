## TASK API
This is a REST API project called TASK API built with Flask, flask-marshmallow, Flask-SQLAlchemy.

## ROUTES TO IMPLEMENTED
| METHOD | ROUTE | FUNCTIONALITY |ACCESS|
| ------- | ----- | ------------- | ------------- |
_Task_|
| *GET* | ```/tasks``` | _List all tasks_|_All tasks_|
| *GET* | ```/tasks?page={page}``` | _List all tasks for different pages_|_All tasks_|
| *POST* | ```/task``` | _Create a task_|_Create task_|
| *GET* | ```task/:id``` | _Get a specific task_|_Retrieve task_|
| *PUT* | ```task/:id``` | _Update a specific task_|_Update task_|
| *DELETE* | ```task/:id``` | Delete a specific task|_Delete task_|

## How to run the Project
- Install Python
- Git clone the project with ```https://github.com/Aderinmola/task_api.git```
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```

- Run ``` .\start.sh ```
- Initial database with ``` flask db init ```
- Create migration script with ``` flask db migrate -m "Initial migration" ```
- Create your database by running ```flask db upgrade```
- Finally run the API, in another terminal
``` python app.py ```
