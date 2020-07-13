from flask_jwt_extended import create_access_token, get_jwt_identity


class JwtActions:
    @staticmethod
    def create_token(id, username):
        data = {'id': id, 'username': username}
        return create_access_token(identity=data)

    @staticmethod
    def get_data_token(token):
        return get_jwt_identity(token)
