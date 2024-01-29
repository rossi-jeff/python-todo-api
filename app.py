from flask import Flask
from flask_restx import  Api
from auth import auth_ns
from todo import todo_ns
from user import user_ns


app = Flask(__name__)
api = Api(
    title="Todo API",
    version="1.0",
    description="ToDo with Authorization"
)

api.add_namespace(auth_ns)
api.add_namespace(todo_ns)
api.add_namespace(user_ns)

api.init_app(app)

app.run(debug=True)
