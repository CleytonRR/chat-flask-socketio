from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from config.jwt import JwtActions
from model.User import User


class AuthController(Resource):
    def post(self):
        try:
            data = request.json
            user = User.query.filter_by(name=data['name']).first()
            response = JwtActions.create_token(user.id, user.name)
        except AttributeError:
            return {"msg": 'User not found'}, 400

        except KeyError:
            return {"msg": 'Require name in format json'}, 400

        except:
            return {"msg": "Error fetching data"}, 400

        return {'token': response}