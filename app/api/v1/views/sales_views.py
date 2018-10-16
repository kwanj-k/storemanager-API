"""
This file contains all the sales related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity


# Local application imports
from app.api.v1.models.sales import Sale
from app.api.v1.models.db import Db
from app.api.v1.views.expect import SaleEtn
from app.api.common.validators import sales_validator


new_s = SaleEtn().sales
v1 = SaleEtn.v1
    
@v1.route('/<int:id>')
class SalesRecords(Resource):
    
    @jwt_required
    def get(self,id):
        """
        Get a specicific sale record
        """

        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        sale = Db.get_s_by_id(id)
        s = None
        if sale.store_id == store_id:
            s = sale
        if s:
            sk = sale.json_dump()
            return {"status":"Success!","data":sk},200
        msg = 'That record does not exist'
        return abort(404,msg)

    @jwt_required
    def delete(self,id):
        """
        Delete a sale
        """
        sale = Db.get_s_by_id(id)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        s = None
        if sale.store_id == store_id:
            s = sale
        if s:
            sk = sale.json_dump()
            Db.sales.remove(sale)
            return {"status":"Deleted!","data":sk},200
        msg = 'That record does not exist'
        return abort(404,msg)

    @jwt_required
    @v1.expect(new_s)
    def put(self,id):
        """
        Update a sale
        """
        s = Db.get_s_by_id(id)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        sale = None
        if s.store_id == store_id:
            sale = s
        if sale is not None:
            msg = 'Sale does not exist'
            abort(404,msg)
        json_data = request.get_json(force=True)
        sales_validator(json_data)
        number = json_data['number']
        s.number = number
        return {"status":"Success!","data":s.json_dump()},200


@v1.route('/')
class SalesRecord(Resource):

    @jwt_required
    def get(self):
        """
        Get all sales
        """
        sales = Db.sales
        if len(sales) < 1:
            msg = 'There are no sale records'
            return abort(404,msg)
        email = get_jwt_identity()
        user = Db.get_user(email=email)
        store_id = user.store_id
        s_list = [s.json_dump() for s in sales if s.store_id == store_id]
        return {"status":"Success!","data":s_list},200
