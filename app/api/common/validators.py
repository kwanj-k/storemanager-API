"""
File with all user input validation methods
"""
# Standard library import
import re
from functools import wraps

# Third party import
from flask import abort
from flask_jwt_extended import get_jwt_identity

# Local app imports
from app.api.v1.models.db import Db



def common(l,d):
    #receive a list and a dict
    #let list be l
    #let dict d
    for i in d.keys():
        if i not in l:
            msg = 'The field {} is not required'.format(i)
            abort(400, msg)
    for i in l:
        if i not in d.keys():
            msg = 'Please provide the {} field'.format(i)
            abort(406, msg)
    for i,v in d.items():
        if not isinstance(v, int):
            gv = "".join(v.split())
            if gv == "":
                msg = 'The {} can not be empty'.format(i)
                abort(406, msg)
                
def commonp(d):
    
    #let dict d
    for i, v in d.items():
        if i == 'name':
            if isinstance(v, int):
                msg = 'Name of the product can not be an integer'
                abort(406, msg)
        if i == 'inventory' or i == 'price':
            if not isinstance(v, int):
                msg = 'Please make sure the {} is a number'.format(i)
                abort(406, msg)




def new_store_validator(k):
    """
    A create new store user input validator
    """

    p_l = ['name', 'category', 'email', 'password']
    common(p_l,k)
    for i, v in k.items():
        if not isinstance(v, str):
            msg = 'The {} field is supposed to be a string'.format(i)
            abort(406, msg)
        if i == 'name' or \
                i == 'category' or i == 'username':
            if len(v) <= 4:
                msg = 'The {} must have atleast five characters'.format(i)
                abort(406, msg)
        if i == 'password':
            if len(i) < 8:
                msg = 'The {} must have atleast eight characters'
                abort(406, msg)
        if i == 'email':
            if not \
                    re.match(r"^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$", v):
                msg = 'Please input a valid email'
                abort(406, msg)


def login_validator(k):
    p_l = ['email', 'password']
    common(p_l,k)


def product_validator(k):
    """
    A create new product user input validator
    """

    pay_load = ['name', 'inventory', 'price']
    common(pay_load,k)
    commonp(k)
    


def product_update_validator(k):
    """
    Product update user input validator
    """

    pay_load = ['name', 'inventory', 'price']
    common(pay_load,k)
    commonp(k)


def sales_validator(k):
    """
    Sales user input validator
    """

    pay_load = ['number']
    common(pay_load,k)
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
        if r == 'Attendant':
            msg = "Only administrators can access these resource"
            abort(406, msg)
        return f(*args, **kwargs)
    return decorator


def super_admin_required(f):
    """ A decorator for restricting certain routes to only superadmin/owner of the store"""
    @wraps(f)
    def decorator(*args, **kwargs):
        current_user = Db.get_user(email=get_jwt_identity())
        r = current_user.role
        if r != 'SuperAdmin':
            msg = "Only Super Admin can access these resource"
            abort(406, msg)
        return f(*args, **kwargs)
    return decorator
