"""
A module to contain all category related test cases
"""
# Standard library imports
import json

# Local application imports
from .base2_config import Settings

c_url = "/api/v2/categories"
p_url = "/api/v2/products"
pc_url = "/api/v2/products/1/category/1"


class TestCategories(Settings):
    data = {
        "name": "Drinks"
    }
    pdata = {
        "name": "SoftDrinks"
    }
    product_data = {
        "name": "monster",
        "inventory": 24,
        "price": 165
    }

    def test_category_addition(self):
        """Test for the add category endpoint."""
        res = self.app.post(c_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_all_categories(self):
        """Test for the get all categories endpoint."""
        self.app.post(c_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.get(c_url)
        self.assertEqual(res.status_code, 200)

    def test_category_update(self):
        """Test for the category update endpoint."""
        self.app.post(c_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.put('/api/v2/categories/1',
                           data=json.dumps(self.pdata),
                           content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_category_delete(self):
        """Test for the category delete endpoint."""
        self.app.post(c_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.delete('/api/v2/categories/1',
                              content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_add_product_to_category(self):
        """Test the add category to a product"""
        self.app.post(p_url,
                      data=json.dumps(self.product_data),
                      content_type='application/json')
        self.app.post(c_url,
                      data=json.dumps(self.data),
                      content_type='application/json')
        res = self.app.post(pc_url,
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)
