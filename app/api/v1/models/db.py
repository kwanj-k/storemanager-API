"""
A db file meant to mimick a database/datastore
"""


class Db:
    """
    Db class contains all the lists of different models
    """
    products = []
    sales = []

    """
    class method to get a product by id
    """
    @classmethod
    def get_p_by_id(cls, id):
        for p in cls.products:
            if p.id == id:
                return p

    """
    method to get product by name
    """
    @classmethod
    def get_product(cls, name):
        for p in cls.products:
            if p.name == name:
                return p

    """
    class method to get a sale record by id
    """
    @classmethod
    def get_s_by_id(cls, id):
        for s in cls.sales:
            if s.id == id:
                return s

    @classmethod
    def get_s_by_product(cls, product):
        for s in cls.sales:
            if s.product == product:
                return s

    @classmethod
    def db_clean(cls):
        cls.sales = []
        cls.products = []
