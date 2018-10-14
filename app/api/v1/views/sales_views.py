"""
This file contains all the sales related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource, Namespace


# Local application imports
from app.api.v1.models.sales import Sale
from app.api.v1.models.db import Db
from app.api.v1.views.expect import SaleEtn
from app.api.common.validators import sales_validator


new_s = SaleEtn().sales
v1 = SaleEtn.v1


@v1.route('/')
class Sales(Resource):
    @v1.expect(new_s)
    def post(self,id):
        json_data = request.get_json(force=True)
        sales_validator(json_data)
        number = json_data['number']
        product = Db.get_p_by_id(id)
        if not product:
            msg = 'Product does not exist'
            res = abort(404,msg)
        price = product.price
        amount = number * price
        if product.inventory < number:
            d = product.inventory
            msg = 'There are only {} {} available'.format(d,product.name)
            return abort(400,msg)
        new_sale = Sale(product.name,number,amount)
        Db.sales.append(new_sale)
        res1 = new_sale.json_dump()
        res =  {"status": "Success!", "data": res1}, 201
        new_inv = product.inventory - number
        product.inventory = new_inv
        return res
