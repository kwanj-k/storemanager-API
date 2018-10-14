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

class SaleEtn:
    """
    Sale model
    """
    v1 = Namespace(
        'sales',
        description='Store manager Api without persitent data storage')
    sales = v1.model('Sale', {
        'product': fields.String(description='The name of the product'),
        'number': fields.Integer(required=True,description='The number of the given products'),
        'amount': fields.Integer(description='The cost of the given number of products')
    })
