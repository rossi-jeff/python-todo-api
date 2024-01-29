from flask_restx import Namespace, Resource

todo_ns = Namespace("todo", description="Endpoints for ToDo")

@todo_ns.route("/<string:todo_id>")
class ToDoById(Resource):

    def get(self):
        return "ToDo by ID"
    
    def patch(self):
        return "Update ToDo"

    def delete(self):
        return "Delete ToDo"

@todo_ns.route("/")
class TodoList(Resource):

    def get(self):
        return "List of Todos"
    
    def post(self):
        return "Create ToDo"

