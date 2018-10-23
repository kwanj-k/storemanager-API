"""
This will contain the base tests configuration.
Thi will be reused/imported in almost all the tests.

"""
# Standard library imports
import unittest
import json

# Local application imports
from app.apps import create_app


config_name = "testing"
app = create_app(config_name)


class Settings(unittest.TestCase):
    """
    Settings class to hold all the similar test config
    """

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
