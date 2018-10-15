"""
File with all user input validation methods
"""

# Third party import
from flask import abort


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
