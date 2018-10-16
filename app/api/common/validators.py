"""
File with all user input validation methods
"""
#Standard library import
import re
from functools import wraps

# Third party import
from flask import abort
from flask_jwt_extended import get_jwt_identity

#Local app imports
from app.api.v1.models.db import Db


def new_store_validator(k):
    """
    A create new store user input validator
    """

    p_l = ['name','category','username','email','password']
    in_k = k.keys()
    for i in in_k:
        if i not in p_l:
            msg = 'Please provide name,category,username,email and password only'
            abort(400,msg)
    for i in p_l:
        if i not in in_k:
            msg = 'The {} field is missing'.format(i)   
            abort(406,msg)
    for i,v in k.items():
        if not isinstance(v, str):
            msg = 'The {} field is supposed to be a string'.format(i)
            abort(406,msg)
        gv = "".join(v.split())
        if gv == "":
            msg = 'The {} can not be empty'.format(i)
            abort(406,msg)
        if i == 'name' or \
            i == 'category' or i == 'username':
            if len(v) <= 4:
                msg = 'The {} must have atleast five characters'.format(i)
                abort(406,msg)
        if i  == 'password':
            if len(i) < 8:
                msg = 'The {} must have atleast eight characters'
                abort(406,msg)
        if i == 'email':
            if not \
                re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$",v):
                msg = 'Please input a valid email'
                abort(406,msg)

def login_validator(k):
    p_l = ['email','password']
    for i in k.keys():
        if i not in p_l:
            msg = 'Please provide email and password only'
            abort(400, msg)
    for x in p_l:
        if x not in k.keys():
            msg = 'Please provide the {} field'.format(x)
            abort(400,msg)

    for i,v in k.items():
        u = "".join(v.split())
        if u == "":
            msg = '{} can not be empty'.format(i)
            abort(406,msg)
        



def product_validator(k):
    """
    A create new product user input validator
    """

    pay_load = ['name', 'inventory', 'price']
    for i in k.keys():
        if i not in pay_load:
            msg = 'Please provide name,inventory and price of the product only'
            abort(400, msg)
    for i, v in k.items():
        if i == 'name':
            if isinstance(v, int):
                msg = 'Name of the product can not be an integer'
                abort(406, msg)
            s = "".join(v.split())
            if s == "":
                msg = 'The product {} cannot be empty'.format(i)
                abort(406, msg)
        if i == 'inventory' or i == 'price':
            if not isinstance(v, int):
                msg = 'Please make sure the {} is a number'.format(i)
                abort(406, msg)
    for i in pay_load:
        if i not in k.keys():
            msg = 'Please provide the {} of the product'.format(i)
            abort(400, msg)

def product_update_validator(k):
    """
    Product update user input validator
    """

    pay_load = ['name', 'inventory', 'price']
    for i in k.keys():
        if i not in pay_load:
            msg = 'Please provide name,inventory and price of the product only'
            abort(400, msg)
    for i, v in k.items():
        if i == 'name':
            if isinstance(v, int):
                msg = 'Name of the product can not be an integer'
                abort(406, msg)
            s = "".join(v.split())
            if s == "":
                msg = 'The product {} cannot be empty'.format(i)
                abort(406, msg)
        if i == 'inventory' or i == 'price':
            if not isinstance(v, int):
                msg = 'Please make sure the {} is a number'.format(i)
                abort(406, msg)


def sales_validator(k):
    """
    Sales user input validator
    """

    pay_load = ['number']
    for i in k.keys():
        if i not in pay_load:
            msg = 'Please provide the number of pruducts only'
            abort(400, msg)
    if 'number' not in k.keys():
        msg = 'Please provide the number of products'
        abort(400, msg)
    for i in k.values():
        if not isinstance(i, int):
            msg = 'Name of the product can not be an integer'
            abort(406, msg)


def admin_required(f):
    """ A decorator for restricting certain routes to only admins"""
    @wraps(f)
    def decorator(*args, **kwargs):
        current_user = Db.get_user(email=get_jwt_identity())
        r = current_user.role
        if r > 1:
            msg = "Only administrators can access these resource"
            abort(406,msg)
        return f(*args, **kwargs)
    return decorator

def super_admin_required(f):
    """ A decorator for restricting certain routes to only superadmin/owner of the store"""
    @wraps(f)
    def decorator(*args, **kwargs):
        current_user = Db.get_user(email=get_jwt_identity())
        r = current_user.role
        if r > 0:
            msg = "Only Super Admin can access these resource"
            abort(406,msg)
        return f(*args, **kwargs)
    return decorator