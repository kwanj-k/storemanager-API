"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.

"""
# Standard library imports
import unittest
import json

# Local application imports
from app.apps import create_app
from app.api.v1.models.db import Db

config_name = "testing"
app = create_app(config_name)

s_url = "/api/v1/stores"
l_url = "/api/v1/login"


class Settings(unittest.TestCase):
    """
    Settings class to hold all the similar test config
    """

    new_s = {
        "name": "Zanamoja",
        "category": "Botique",
        "username": "kwanj",
        "email": "kwanj@kwanjt.com",
        "password": "passwordroot"
    }

    l_data = {
        "email": "kwanj@kwanjt.com",
        "password": "passwordroot"
    }

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def autheniticate(self):
        self.app.post(s_url,
                      data=json.dumps(self.new_s),
                      content_type='application/json')
        return self.app.post(l_url,
                             data=json.dumps(self.l_data),
                             content_type='application/json')

    def tearDown(self):
        Db.products = []
        Db.sales = []
