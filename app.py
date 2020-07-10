from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class InitialRoute(Resource):
    def get(self):
        return {'Message': 'It works'}

api.add_resource(InitialRoute, '/')

if __name__ == '__main__':
    app.run(debug=True)