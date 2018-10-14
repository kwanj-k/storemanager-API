"""
A db file meant to mimick a database/datastore
"""


class Db:
    """
    Db class contains all the lists of different models
    """
    products = []

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
