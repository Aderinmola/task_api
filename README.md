## TASK API
This is a REST API project called TASK API built with Flask, flask-marshmallow, Flask-SQLAlchemy.


## How to run the Project
- Install Python
- Git clone the project with ```https://github.com/Aderinmola/task_api.git```
- change directory with ``` cd task_api ``` 
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with ``` pip install -r requirements.txt ```
- Initial database with ``` flask db init ```
- Create migration script with ``` flask db migrate -m "Initial migration" ```
- Create your database by running ```flask db upgrade```
- Finally run the API, in another terminal
``` python app.py ```
- Go ahead to test the endpoints listed in the table below with postman, using the base url ``` http://127.0.0.1:5000/```


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
