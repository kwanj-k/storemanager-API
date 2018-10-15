"""
A module to contain all sale related test cases
"""
# Standard library imports
import json

# Local application imports
from .base_config import Settings
from app.api.v1.models.db import Db

s_url = "/api/v1/sales"
p_url = "/api/v1/products"


class TestProducts(Settings):
    """
    p_data to contain product data
    """
    p_data = {
        "name": "monster",
        "inventory": 24,
        "price": 165
    }
    s_data = {
        "number": 3
    }
    m_data = {
        "number": 387
    }
    ns_data = {
        "number": 12
    }
    str_data = {
        "number": 'tr'
    }
    unwanted_data = {
        "number": 12,
        "yes":"yes"
    }
    no_data = {
    }

    def test_make_sale(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.post("/api/v1/products/{}".format(p.id),
                            data=json.dumps(self.s_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_make_sale_with_str_number(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.post("/api/v1/products/{}".format(p.id),
                            data=json.dumps(self.str_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)

    def test_selling_non_existing_product(self):
        """Test for the make sale endpoint."""
        res = self.app.post("/api/v1/products/1",
                            data=json.dumps(self.s_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_make_sale_with_morenum_than_available(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.post("/api/v1/products/{}".format(p.id),
                            data=json.dumps(self.m_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_make_sale_with_no_num(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.post("/api/v1/products/{}".format(p.id),
                            data=json.dumps(self.no_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_make_sale_with_unwanted_data(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.post("/api/v1/products/{}".format(p.id),
                            data=json.dumps(self.unwanted_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_get_all_sales(self):
        """Test for the get all sales endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        self.app.post("/api/v1/products/{}".format(p.id),
                      data=json.dumps(self.s_data),
                      content_type='application/json')
        res = self.app.get(s_url)
        self.assertEqual(res.status_code, 200)

    def test_get_sales_with_no_records(self):
        """Test for the get all sales endpoint."""
        res = self.app.get(s_url)
        self.assertEqual(res.status_code, 404)

    def test_get_sale_by_id(self):
        """Test for the get sale by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        self.app.post("/api/v1/products/{}".format(p.id),
                      data=json.dumps(self.s_data),
                      content_type='application/json')
        s = Db.get_s_by_product('monster')
        res = self.app.get("/api/v1/sales/{}".format(s.id))
        self.assertEqual(res.status_code, 200)


    def test_get_sale_by_id_that_doesnot_exist(self):
        """Test for the get sale by id endpoint."""
        res = self.app.get("/api/v1/sales/1")
        self.assertEqual(res.status_code, 404)

    def test_sale_delete(self):
        """Test for the delete sale by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        self.app.post("/api/v1/products/{}".format(p.id),
                      data=json.dumps(self.s_data),
                      content_type='application/json')
        s = Db.get_s_by_product('monster')
        res = self.app.delete("/api/v1/sales/{}".format(s.id))
        self.assertEqual(res.status_code, 200)


    def test_deletion_of_nonexisting_sale(self):
        """Test for the delete sale by id endpoint."""
        res = self.app.delete("/api/v1/sales/1")
        self.assertEqual(res.status_code, 404)

    def test_sale_update(self):
        """Test for the update sale by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        p = Db.get_product('monster')
        self.app.post("/api/v1/products/{}".format(p.id),
                      data=json.dumps(self.s_data),
                      content_type='application/json')
        s = Db.get_s_by_product('monster')
        res = self.app.put("/api/v1/sales/{}".format(s.id),
                        data=json.dumps(self.ns_data),
                      content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_updating_sale_that_doesnot_exist(self):
        """Test for the update sale by id endpoint."""
        res = self.app.put("/api/v1/sales/1",
                        data=json.dumps(self.ns_data),
                      content_type='application/json')
        self.assertEqual(res.status_code, 404)
