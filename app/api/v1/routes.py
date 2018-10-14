from flask import Blueprint,request
from flask_restplus import Api,Resource,fields


from .views.products_views import v1 as p_r


v_1 = Blueprint('v_1', __name__, url_prefix="/api/v1")
api = Api(v_1)
v1 = api.namespace('v1',description = 'Store manager Api without persitent data storage')

api.add_namespace(p_r, path="/products")