from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
import os
from controllers.user_controller import UserController
from controllers.auth_controller import AuthController

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_KEY")
jwt = JWTManager(app)
api = Api(app)


api.add_resource(UserController, '/')
api.add_resource(AuthController, '/auth')

if __name__ == '__main__':
    app.run(debug=True)
