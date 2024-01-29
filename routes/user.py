from flask_restx import Namespace, Resource

user_ns = Namespace("user", description="Endpoints for User")

@user_ns.route("/current")
class UserCurrent(Resource):
    def get(self):
        return "Current User"

@user_ns.route("/change")
class UserPW(Resource):
    def patch(self):
        return "Change Password"


@user_ns.route("/<string:user_id>")
class UserById(Resource):
    def get(self):
        return "User by Id"
    
    def patch(self):
        return "Update User"
    
    def delete(self):
        return "Delete User"
