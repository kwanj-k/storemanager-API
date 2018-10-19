"""
This file contains all the account models
Store
SuperAdmin
Admin
Attendant
"""


# Third party import
from werkzeug.security import generate_password_hash

"""
pk :variable used to generate ids
"""


class Store:
    pk = 1

    def __init__(self, name, category):
        self.id = Store.pk
        self.name = name
        self.category = category
        Store.pk += 1

    def json_dump(self):
        """
        custom json_dump method to return a custom python dict in response
        """
        return dict(
            store_name=self.name,
            category=self.category
        )


class User:
    pk = 1

    def __init__(self, store_id,role, email, password):
        self.id = User.pk
        self.store_id = store_id
        self.email = email
        self.role = role
        self.password = generate_password_hash(password)
        User.pk += 1

    def json_dump(self):
        """
        custom json_dump method to return a custom python dict in response
        """
        if self.role == 0:
            self.role = 'SuperAdmin'
        if self.role == 1:
            self.role == 'Admin'
        if self.role == 2:
            self.role == 'Attendant'
        return dict(
            email=self.email,
            role=self.role)
