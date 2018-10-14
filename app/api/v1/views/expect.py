"""
A file to model all input expectations
"""
from flask_restplus import fields, Namespace


class ProductEtn:
    """
    Product input data expectations
    """
    v1 = Namespace(
        'products',
        description='Store manager Api without persitent data storage')
    products = v1.model('Product', {
        'name': fields.String(required=True, description='The name of the product'),
        'inventory': fields.Integer(required=True, description='The number of the given products'),
        'price': fields.Integer(required=True, description='The price of the product')
    })
