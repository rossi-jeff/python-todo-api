from flask_restx import Namespace, Resource

auth_ns = Namespace("auth", description="Endpoints for Authorization")

@auth_ns.route("/register")
class AuthRegister(Resource):
    @auth_ns.doc("Register")
    def post(self):
        return "Register Method"


@auth_ns.route("/login")
class AuthLogin(Resource):
    @auth_ns.doc("Login")
    def post(self):
        return "Login Method"
