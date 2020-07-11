from flask import Flask
from flask_restful import Api
from controllers.user_controller import UserController

app = Flask(__name__)
api = Api(app)


api.add_resource(UserController, '/')

if __name__ == '__main__':
    app.run(debug=True)
