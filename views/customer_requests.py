CUSTOMERS = [
    {
        "id": 1,
        "email": "ryan@ryan.com",
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "email": "alvin@chipmunks.com",
        "name": "Alvin"
    },
    {
        "id": 3,
        "email": "simon@chipmunks.com",
        "name": "Simon"
    },
    {
        "id": 4,
        "email": "theodore@chipmunks.com",
        "name": "Theodore"
    }
]

def get_all_customers():
    """Returns list of dictionaries stored in CUSTOMERS variable"""
    return CUSTOMERS


# Function with a single parameter
def get_single_customer(id):
    """Returns dictionary of single customer from list stored in CUSTOMERS or returns nothing."""
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    """Args: customer (json string), returns new dictionary with id property added"""
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    """Function deletes a single customer by id. arg of id"""
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
