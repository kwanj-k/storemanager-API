"""
A file to model the product object
"""

class Product:
    """
    pk :Primary key to make the product id
    """
    pk = 1
    def __init__(self,name,inventory,price):
        self.id = Product.pk
        self.name = name
        self.inventory = inventory
        self.price = price
        Product.pk += 1

    def json_dump(self):
        return dict(
            name = self.name,
            inventory = self.inventory,
            price = self.price
        )