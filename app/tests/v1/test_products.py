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
    d_data = {
        "name": 55,
        "inventory": 24,
        "price": 165
    }
    str_data = {
        "name": "monster",
        "inventory": '24',
        "price": '165'
    }
    e_name = {
        "name":"  ",
        "inventory": 24,
        "price": 165
    }
    unwanted_data = {
        "name": "monster",
        "inventory": 24,
        "price": 165,
        "test": 165
    }
    no_name = {
        "inventory": 24,
        "price": 165
    }

    def test_product_addition(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_product_addition_with_digit_name(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.d_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)

    def test_product_addition_with_str_price_inventory(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.str_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)

    def test_product_double_addition(self):
        """Test for the add product endpoint."""
        self.app.post(p_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        res = self.app.post(p_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)


    def test_product_addition_with_unwanted_data(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.unwanted_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_product_addition_with_empty_namme(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.e_name),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)
    
    def test_product_addition_with_no_namme(self):
        """Test for the add product endpoint."""
        res = self.app.post(p_url,
                            data=json.dumps(self.no_name),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_get_all_products(self):
        """Test for the get all products endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.get(p_url)
        self.assertEqual(res.status_code, 200)

    def test_get_products_without_any_in_system(self):
        """Test for the get all products endpoint."""
        res = self.app.get(p_url)
        self.assertEqual(res.status_code, 404)

    def test_get_product_by_id(self):
        """Test for the get product by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        res = self.app.get("/api/v1/products/{}".format(p.id))
        self.assertEqual(res.status_code, 200)

    def test_get_product_that_does_not_exist(self):
        """Test for the get product by id endpoint."""
        res = self.app.get("/api/v1/products/1")
        self.assertEqual(res.status_code, 404)

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

    def test_product_update_with_str_price_inventory(self):
        """Test for the product update endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.put(url,
                        data=json.dumps(self.str_data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 406)

    def test_product_update_with_int_name(self):
        """Test for the product update endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.put(url,
                        data=json.dumps(self.d_data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 406)

    def test_non_existing_product_update(self):
        """Test for the product update endpoint."""
        url = "/api/v1/products/1"
        res = self.app.put(url,
                        data=json.dumps(self.data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 404)

    def test_product_update_with_unwanted_data(self):
        """Test for the add product endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.put(url,
                        data=json.dumps(self.unwanted_data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_product_update_with_empty_name(self):
        """Test for the add product endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        p = Db.get_product('monster')
        url = "/api/v1/products/{}".format(p.id)
        res = self.app.put(url,
                        data=json.dumps(self.e_name),
                        content_type='application/json')
        self.assertEqual(res.status_code, 406)

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

    def test_non_existing_product_delete(self):
        """Test for the product delete endpoint."""
        url = "/api/v1/products/1"
        res = self.app.delete(url,
                        data=json.dumps(self.data),
                        content_type='application/json')
        self.assertEqual(res.status_code, 404)
