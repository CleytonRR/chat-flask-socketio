from flask import request
from flask_restful import Resource
from model.User import User


class UserController(Resource):
    def post(self):
        try:
            dados = request.json
            user = User(name=dados['name'], email=dados['email'], password=dados['password'])
            user.save()
            response = {'Name: ': user.name, 'Email: ': user.email,
                        'Password: ': user.password}
        except:
            response = {
                'Message': 'Erro ao receber dados'
            }
            return response, 400
        return response, 200
