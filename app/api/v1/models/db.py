"""
A db file meant to mimick a database/datastore
"""



def method_helper(mlist,mitem):
    for p in mlist:
        if p.mitem == mitem:
            return p


class Db:
    """
    Db class contains all the lists of different models
    """

    stores = []
    users = []
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
    method to get user by email
    """
    @classmethod
    def get_user(cls, email):
        for e in cls.users:
            if e.email == email:
                return e

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

    """
    method to get store by name
    """
    @classmethod
    def get_store(cls, name):
        for s in cls.stores:
            if s.name == name:
                return s
