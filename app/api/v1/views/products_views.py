"""
This file contains all the product related resources

"""

# Third party imports
from flask import request, json
from flask_restplus import Resource, Namespace


# Local application imports
from app.api.v1.models.products import Product
from app.api.v1.models.db import Db
from app.api.v1.views.expect import ProductEtn
from app.api.common.validators import product_validator


new_p = ProductEtn().products
v1 = ProductEtn().v1


@v1.route('/')
class Products(Resource):
    @v1.expect(new_p)
    def post(self):
        json_data = request.get_json(force=True)
        product_validator(json_data)
        new_product = Product(json_data['name'],
                              json_data['inventory'],
                              json_data['price'])
        Db.products.append(new_product)
        res = new_product.json_dump()
        return {"status": "Success!", "data": res}, 201
