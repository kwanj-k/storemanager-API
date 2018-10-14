"""
This file contains all the version one routes
"""

# Third party imports
from flask import Blueprint, request
from flask_restplus import Api, Resource, fields


# Local application imports
from .views.products_views import v1 as pro_routes
from .views.sales_views import v1 as sales_routes


v_1 = Blueprint('v_1', __name__, url_prefix="/api/v1")
api = Api(v_1)
v1 = api.namespace(
    'v1',
    description='Store manager Api without persitent data storage')

api.add_namespace(pro_routes, path="/products/")
api.add_namespace(sales_routes, path="/sales")
