"""
A file to model the sale object
"""


class Sale:
    """
    pk :Primary key to make the sale id
    """
    pk = 1

    def __init__(self, store_id, product, number, amount):
        """
        Product constructor
        """
        self.id = Sale.pk
        self.store_id = store_id
        self.product = product
        self.number = number
        self.amount = amount
        Sale.pk += 1

    def json_dump(self):
        """
        custom json_dump method to return a custom python dict in response
        """
        return dict(
            id=self.id,
            product=self.product,
            number=self.number,
            amount=self.amount
        )
