"""
A module to contain all sale related test cases
"""
# Standard library imports
import json

# Local application imports
from .base_config import Settings

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

    def test_make_sale(self):
        """Test for the make sale endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        res = self.app.post("/api/v1/products/1")
        self.assertEqual(res.status_code, 201)

    def test_get_all_sales(self):
        """Test for the get all sales endpoint."""
        res = self.app.get(s_url)
        self.assertEqual(res.status_code, 200)

    def test_get_sale_by_id(self):
        """Test for the get sale by id endpoint."""
        self.app.post(p_url,
                      data=json.dumps(self.p_data),
                      content_type='application/json')
        self.app.post("/api/v1/products/1")
        res = self.app.get("/api/v1/sales/1")
        self.assertEqual(res.status_code, 200)
