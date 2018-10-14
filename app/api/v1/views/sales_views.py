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
    
@v1.route('/<int:id>')
class SalesRecords(Resource):
    def get(self,id):
        sale = Db.get_s_by_id(id)
        if sale:
            sk = sale.json_dump()
            return {"status":"Success!","data":sk},200
        msg = 'That record does not exist'
        return abort(404,msg)

@v1.route('/')
class SalesRecord(Resource):
    def get(self):
        sales = Db.sales
        if len(sales) < 1:
            msg = 'There are no sale records'
            return abort(404,msg)
        s_list = [s.json_dump() for s in sales]
        return {"status":"Success!","data":s_list},200
