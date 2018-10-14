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
    ns_data = {
        "number": 12
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
