"""
This file contains all the product related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity


# Local application imports
from app.api.v1.models.products import Product
from app.api.v1.models.sales import Sale
from app.api.v1.models.db import Db
from app.api.v1.views.expect import ProductEtn,SaleEtn
from app.api.common.validators import product_validator,sales_validator,product_update_validator,admin_required


new_p = ProductEtn().products

v1 = ProductEtn().v1


@v1.route('')
class Products(Resource):

    @jwt_required
    @admin_required
    @v1.expect(new_p)
    def post(self):
        """
        Add a product to the manager
        """
        json_data = request.get_json(force=True)
        product_validator(json_data)
        p = Db.get_product(json_data['name'])
        if p:
            msg = 'Product already exists.Update product inventory instead'
            abort(406,msg)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        new_product = Product(store_id,json_data['name'],
                              json_data['inventory'],
                              json_data['price'])
        Db.products.append(new_product)
        res = new_product.json_dump()
        return {"status": "Success!", "data": res}, 201

    @jwt_required
    def get(self):
        """
        Get all products
        """
        products = Db.products
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        res = [p.json_dump() for p in products if p.store_id == store_id]
        if len(products) < 1:
            msg = 'There are no products at this time'
            abort(404,msg)
        return res

new_s = SaleEtn().sales

@v1.route('<int:id>')
class Products1(Resource):
    @jwt_required
    @v1.expect(new_s)
    def post(self,id):
        """
        Sell product
        """
        json_data = request.get_json(force=True)
        sales_validator(json_data)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        number = json_data['number']
        product = Db.get_p_by_id(id)
        if  product:
            price = product.price
            amount = number * price
            if product.inventory < number:
                d = product.inventory
                msg = 'There are only {} {} available'.format(d,product.name)
                return abort(400,msg)
            new_sale = Sale(store_id,product.name,number,amount)
            Db.sales.append(new_sale)
            res1 = new_sale.json_dump()
            new_inv = product.inventory - number
            product.inventory = new_inv
            return {"status": "Success!", "data": res1}, 201
        msg = 'Product does not exist'
        return {"message":msg},404

    @jwt_required
    def get(self,id):
        """
        Get a specific product
        """

        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        p = Db.get_p_by_id(id)
        product = None
        if p.store_id == store_id:
            p = product
        if product is None:
            msg = 'Product does not exist'
            abort(404,msg)
        return {"status":"Success","data":product.json_dump()},200

    @jwt_required
    @admin_required
    @v1.expect(new_p)
    def put(self,id):
        """
        Edit a product
        """
        p = Db.get_p_by_id(id)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        product = None
        if p.store_id != store_id:
            p = product
        if p is None:
            msg = 'Product does not exist'
            abort(404,msg)
        json_data = request.get_json(force=True)
        product_update_validator(json_data)
        name = json_data['name']
        inventory = json_data['inventory']
        price = json_data['price']
        if name:
            p.name = name
        if inventory:
            p.inventory = inventory
        if price:
            p.price = price
        return {"status":"Success!","data":p.json_dump()},200

    @jwt_required
    @admin_required
    def delete(self,id):
        """
        Delete a product
        """
        p = Db.get_p_by_id(id)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        product = None
        if p.store_id != store_id:
            p = product
        if p is None:
            msg = 'Product does not exist'
            abort(404,msg)
        Db.products.remove(p)
        return {"status":"Deleted!","data":p.json_dump()},200

        
        
