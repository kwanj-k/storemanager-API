"""
This file contains all the accounts related resources

"""

# Third party imports
from flask import request, json, abort
from flask_restplus import Resource


# Local application imports
from app.api.v1.models.accounts import Store,SuperAdmin
from app.api.v1.models.db import Db
from app.api.v1.views.expect import StoreEtn
from app.api.common.validators import new_store_validator

new_store = StoreEtn.stores

v1 = StoreEtn().v1


@v1.route('')
class Stores(Resource):
    @v1.expect(new_store)
    def post(self):
        json_data = request.get_json(force=True)
        new_store_validator(json_data)
        check = Db.get_store(json_data['name'])
        if check:
            msg = 'Store name is already taken'
            abort(406,msg)
        new_store= Store(json_data['name'],
                              json_data['category'])
        Db.stores.append(new_store)
        store = Db.get_store(json_data['name'])
        store_id = store.id
        new_sadmin = SuperAdmin(store_id,
                                json_data['username'],
                                json_data['email'],
                                json_data['password'])
        Db.users.append(new_sadmin)
        res1 = new_store.json_dump()
        res2 = new_sadmin.json_dump()
        return {"status": "Success!", "store": res1,"owner":res2}, 201