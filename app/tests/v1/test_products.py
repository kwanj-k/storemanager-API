"""
A module to contain all product related test cases
"""
# Standard library imports
import json

# Local application imports
from .base_config import Settings
from app.api.v1.models.db import Db

p_url = "/api/v1/products"


class TestProducts(Settings):
    """
    data variable to contain product data
    """
    data = {
        "name": "monster",
        "inventory": 24,
        "price": 165
    }

    def test_product_addition(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_all_products(self):
        """Test for the get all products endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.get(p_url)
        self.assertEqual(res.status_code, 200)

    def test_get_product_by_id(self):
        """Test for the get product by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.get("/api/v1/products/{}".format(p.id))
        self.assertEqual(res.status_code, 200)

    def test_product_update(self):
        """Test for the product update endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.put(url,
                        data=json.dumps(self.data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_product_delete(self):
        """Test for the product delete endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.delete(url,
                        data=json.dumps(self.data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 200)
