"""
File with all user input validation methods
"""

# Third party import
from flask import abort


def space_stripper(k):
    """
    Method to remove white space from inputs
    """

    for i, v in k.items():
        try:
            stripped = "".join(v.split())
            if stripped == "":
                msg = 'The field {} cannot be empty'.format(i)
                abort(406, msg)
        except BaseException:
            continue


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
            if v.isdigit():
                msg = 'Name of the product can not be an integer'
                abort(400, msg)
            s = "".join(v.split())
            if s == "":
                msg = 'The product {} cannot be empty'.format(i)
                abort(406, msg)
        if i == 'inventory' or i == 'price':
            try:
                int(v)
            except BaseException:
                msg = 'Please make sure the {} is a number'.format(i)
                abort(400, msg)
    for i in pay_load:
        if i not in k.keys():
            msg = 'Please provide the {} of the product'.format(i)
            abort(400, msg)


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
        try:
            int(i)
        except BaseException:
            msg = 'The number of products should be a number'
            abort(406, msg)
