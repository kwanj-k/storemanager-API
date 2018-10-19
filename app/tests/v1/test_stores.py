"""
A module to contain all store related test cases
"""
# Standard library imports
import json

# Local application imports
from .base_config import Settings
from app.api.v1.models.db import Db

s_url = "/api/v1/stores"


class TestStores(Settings):
    data = {
        "name": "Zanaseee",
        "category": "Botique",
        "email": "kwanj@kwanj.com",
        "password": "passwordroot"
    }
    unwanted_data = {
        "name": "Zanas",
        "category": "Botique",
        "email": "kwanj@kwanj.com",
        "password": "passwordroot",
        "tehdeh": "yreugfrjdk"
    }
    m_data = {
        "category": "Botique",
        "email": "kwanj@kwanj.com",
        "password": "passwordroot"
    }

    def test_store_creation(self):
        """Test for the add store endpoint."""
        res = self.app.post(s_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_store_addition_with_unwanted_data(self):
        """Test for the add store endpoint."""
        res = self.app.post(s_url,
                            data=json.dumps(self.unwanted_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 400)

    def test_store_addition_with_missing_fields(self):
        """Test for the add store endpoint."""
        res = self.app.post(s_url,
                            data=json.dumps(self.m_data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 406)
