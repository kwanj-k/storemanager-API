"""
A file to model the product object
"""


class Product:
    """
    pk :Primary key to make the product id
    """
    pk = 1

    def __init__(self,store_id, name, inventory, price):
        """
        Product constructor
        """
        self.id = Product.pk
        self.store_id = store_id
        self.name = name
        self.inventory = inventory
        self.price = price
        Product.pk += 1

    def json_dump(self):
        """
        custom json_dump method to return a custom python dict in response
        """
        return dict(
            name=self.name,
            inventory=self.inventory,
            price=self.price
        )
