"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.

"""
# Standard library imports
import unittest

# Local application imports
from app.apps import create_app
from app.api.v1.models.db import Db

config_name = "testing"
app = create_app(config_name)


class Settings(unittest.TestCase):
    """
    Settings class to hold all the similar test config
    """

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        Db.products = []
        Db.sales = []
        
