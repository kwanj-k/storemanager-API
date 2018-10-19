"""
This file contains all the auth related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity


# Local application imports
from app.api.v1.models.accounts import User
from app.api.v1.models.db import Db
from app.api.v1.views.expect import UserEtn
from app.api.common.validators import login_validator, admin_required, super_admin_required

user_login = UserEtn().users

v1 = UserEtn().v1


@v1.route('auth/login')
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
        if u is None or not check_password_hash(u.password, epass):
            msg = 'Invalid credentials'
            abort(400, msg)
        access_token = create_access_token(identity=json_data['email'])
        return {"status": "Success!", "token": access_token}, 200


@v1.route('admin')
class AddAdmin(Resource):
    @v1.doc( security='apikey')
    @jwt_required
    @super_admin_required
    @v1.expect(user_login)
    def post(self):
        """
        Add Admin
        """  
        json_data = request.get_json(force=True)
        login_validator(json_data)
        email = get_jwt_identity()
        newad = Db.get_user(json_data['email'])
        if newad and newad.role <= 1:
            msg = "User is Admin already"
            abort(406, msg)
        user = Db.get_user(email=email)
        store_id = user.store_id
        role = 1
        user_reg = User(store_id,
                         role,
                         json_data['email'],
                         json_data['password'])
        for i, item in enumerate(Db.users):
            if item == newad:
                Db.users[i] = user_reg
        Db.users.append(user_reg)
        return {"status": "Success!", "data": user_reg.json_dump()}, 201


@v1.route('attendant')
class AddAttendant(Resource):
    @v1.doc( security='apikey')
    @jwt_required
    @admin_required
    @v1.expect(user_login)
    def post(self):
        """
        Add Attendant
        """
        json_data = request.get_json(force=True)
        login_validator(json_data)
        newatt = Db.get_user(json_data['email'])
        if newatt and newatt.role == 2:
            msg = "User is Attendant already"
            abort(406, msg)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        role = 2
        user_reg = User(store_id,
                             role,
                             json_data['email'],
                             json_data['password'])
        newatt = Db.get_user(json_data['email'])
        for k, j in enumerate(Db.users):
            if j == newatt:
                Db.users[k] = user_reg
        Db.users.append(user_reg)
        return {"status": "Success!", "data": user_reg.json_dump()}, 201
