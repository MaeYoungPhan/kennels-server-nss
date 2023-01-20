import sqlite3
import json
from models import Employee, Location

EMPLOYEES = EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Bobby McGee"
    },
    {
        "id": 3,
        "name": "Maggie Mae"
    }
]

def get_all_employees():
    """Returns list of dictionaries stored in EMPLOYEES variable"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            e.animal_id,
            l.name location_name,
            l.address location_address
        FROM employee e
        JOIN location l
            ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all customer representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Employee class above.
            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'], row['animal_id'])
            
            # Create a Location instance from the current row
            location = Location(row['id'], row['location_name'], row['location_address'])

            del location.id

            # Add the dictionary representation of the location to the animal
            employee.location = location.__dict__

            employees.append(employee.__dict__)

    return employees


# Function with a single parameter
def get_single_employee(id):
    """Returns dictionary of single employee from list stored in EMPLOYEES or returns nothing."""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id,
            e.animal_id
        FROM employee e
        WHERE e.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['address'],
                            data['location_id'], data['animal_id'])

        return employee.__dict__

def get_employees_by_location(location):
    """Returns a list of dict. of all employees at location_id x"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            e.id,
            e.name,
            e.address,
            e.location_id,
            e.animal_id
        from Employee e
        WHERE e.location_id = ?
        """, ( location, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['address'], row['location_id'], row['animal_id'])
            employees.append(employee.__dict__)

    return employees

def create_employee(new_employee):
    """Args: employee (json string), returns new dictionary with id property added"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, address, location_id, animal_id )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_employee['name'], new_employee['address'],
            new_employee['locationId'], new_employee['animalId'] ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the employee dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_employee['id'] = id

    return new_employee


def delete_employee(id):
    """Deletes single employee by id. Args: id(int), Returns: """""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM employee
        WHERE id = ?
        """, (id, ))


def update_employee(id, new_employee):
    """args int id, json string employee, function finds employee dictionary, replaces with new one """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                address = ?,
                location_id = ?,
                animal_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['address'],
            new_employee['location_id'], new_employee['animal_id'], id ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
