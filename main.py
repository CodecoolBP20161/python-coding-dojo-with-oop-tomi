class Contact:
    '''Write a "Contact" class in which you can store contact information with name and email.'''

    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = []


class Supplier(Contact):

    all_orders = {}

    def __init__(self, name, email):
        super().__init__(name, email)

    @classmethod
    def order(cls, string):
        cls.all_orders['self.email'] = string
