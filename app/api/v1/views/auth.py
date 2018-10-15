"""
This file contains all the auth related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required,create_access_token,get_jwt_identity


# Local application imports
from app.api.v1.models.accounts import Admin,Attendant
from app.api.v1.models.db import Db
from app.api.v1.views.expect import UserEtn
from app.api.common.validators import login_validator

user_login = UserEtn().users

v1 = UserEtn().v1

@v1.route('login')
class Login(Resource):
    @v1.expect(user_login)
    def post(self):
        """
        Login
        """
        json_data = request.get_json(force=True)
        login_validator(json_data)
        u = Db.get_user(json_data['email'])
        epass = json_data['password']
        if u is None or not check_password_hash(u.password,epass):
            msg = 'Invalid credentials'
            abort(400,msg)
        access_token = create_access_token(identity=json_data['email'])
        return {"status":"Success!","token":access_token},200