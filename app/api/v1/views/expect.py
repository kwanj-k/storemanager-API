"""
A file to model all input expectations
"""
from flask_restplus import fields, Namespace



class StoreEtn:
    """
    Store input data expectations
    """
    v1 = Namespace(
        'stores',
        description='Stores')
    stores = v1.model('Store', {
        'name': fields.String(required=True, description='The name of the store'),
        'category': fields.String(required=True, description='The category of the store'),
        'username': fields.String(required=True, description='The owner/superadmin of the store'),
        'email': fields.String(required=True, description='The owners/stores email address'),
        'password': fields.String(required=True, description='The owners password')
    })


class UserEtn:
    """
    User login input data expectations
    """
    v1 = Namespace(
        'users',
        description='Users')
    users = v1.model('User', {
        'username': fields.String(description='The name of user'),
        'email': fields.String(required=True, description='The user"s email address'),
        'password': fields.String(required=True, description='The user"s password')
    })


class ProductEtn:
    """
    Product input data expectations
    """
    v1 = Namespace(
        'products',
        description='Products related endpoints')
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
        description='Sales related endpoints')
    sales = v1.model('Sale', {
        'product': fields.String(description='The name of the product'),
        'number': fields.Integer(required=True,description='The number of the given products'),
        'amount': fields.Integer(description='The cost of the given number of products')
    })
