"""
This file contains all the product related resources

"""

# Third party imports
from flask import request, json, abort
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
        p = Db.get_product(json_data['name'])
        if p:
            msg = 'Product already exists.Update product inventory instead'
            abort(406,msg)
        new_product = Product(json_data['name'],
                              json_data['inventory'],
                              json_data['price'])
        Db.products.append(new_product)
        res = new_product.json_dump()
        return {"status": "Success!", "data": res}, 201
    def get(self):
        products = Db.products
        res = [p.json_dump() for p in products]
        if len(products) < 1:
            msg = 'There are no products at this time'
            res = abort(404,msg)
        return res


@v1.route('/<int:id>')
class ProductsDetails(Resource):
    def get(self,id):
        product = Db.get_p_by_id(id)
        if product:
            return {"status":"Success","data":product.json_dump()}
        msg = 'Product does not exist'
        res = abort(404,msg)
        return res
