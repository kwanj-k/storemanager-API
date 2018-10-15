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


@v1.route('admin')
class AddAdmin(Resource):
    @jwt_required
    @v1.expect(user_login)
    def post(self):
        """
        Add Admin
        """
        json_data = request.get_json(force=True)
        login_validator(json_data)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = 1
        if 'username' in json_data:
            username = json_data['username']
        username = None
        user_reg = Admin(store_id,
                    username,
                    json_data['email'],
                    json_data['password'])
        newad =Db.get_user(json_data['email'])
        # if newad.role == 1:
        #     return {"message":"User is Admin already"},406
        for i,item in enumerate(Db.users):
            if item==newad:
                Db.users[i]= user_reg
        Db.users.append(user_reg)
        return {"status":"Success!","data": user_reg.json_dump()}