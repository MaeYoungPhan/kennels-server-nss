class Customer():
    """Class initializer to create customer objects"""
    # Class initializer. It has 3 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
