"""
A module to contain all authorisation related test cases
"""
# Standard library imports
import json

# Local application imports
from .base_config import Settings
from app.api.v1.models.db import Db

l_url = "/api/v1/login"
s_url = "/api/v1/stores"
a_url = "/api/v1/admin"
att_url = "/api/v1/attendant"


class TestAuth(Settings):
    s_data = {
        "name": "Zanas",
        "category": "Botique",
        "username": "kwanj",
        "email": "kwanj@kwanj.com",
        "password": "passwordroot"
    }
    data = {
        "email": "kwanj@kwanj.com",
        "password": "passwordroot"
    }

    def test_login(self):
        """Test for the login endpoint."""
        self.app.post(s_url,
                      data=json.dumps(self.s_data),
                      content_type='application/json')
        res = self.app.post(l_url,
                            data=json.dumps(self.data),
                            content_type='application/json')
        self.assertEqual(res.status_code, 200)

    def test_addadmin(self):
        """
        Test add admin
        """
        login = self.autheniticate()
        token = json.loads(login.data.decode()).get('token')
        res = self.app.post(a_url,
                            data=json.dumps(self.data),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_addattendant(self):
        """
        Test add attendant
        """
        login = self.autheniticate()
        token = json.loads(login.data.decode()).get('token')
        res = self.app.post(att_url,
                            data=json.dumps(self.data),
                            headers=dict(Authorization="Bearer " + token),
                            content_type='application/json')
        self.assertEqual(res.status_code, 201)
