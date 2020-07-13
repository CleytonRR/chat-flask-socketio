from flask import request
from flask_restful import Resource
from model.User import User
from utils.verify_email import VerifyEmail
from exceptions.email_exception import EmailException


class UserController(Resource):
    def post(self):
        try:
            dados = request.json
            user = User(name=dados['name'], email=dados['email'], password=dados['password'])
            if not VerifyEmail.verify(dados['email']):
                raise EmailException()
            user.save()
            response = {'Name: ': user.name, 'msg': 'Save success'}

        except EmailException:
            response = {
                'msg': 'Invalid email'
            }

            return response, 400

        except KeyError:
            response = {
                'msg': 'It is necessary to send username, email and password in json format'
            }
            return response, 400
        except:
            response = {
                'msg': 'Error receiving data'
            }
            return response, 400

        return response, 201
