import random


def generate_employee_data():

    number = random.randint(
        10000,
        99999
    )

    return {
        "first_name": f"Auto{number}",
        "middle_name": "Test",
        "last_name": "Employee",
        "employee_id": f"E{number}"
    }


def generate_candidate_data():

    number = random.randint(
        10000,
        99999
    )

    return {
        "first_name": f"Candidate{number}",
        "middle_name": "Auto",
        "last_name": "Test",
        "email": f"candidate{number}@example.com"
    }


def generate_username():

    number = random.randint(
        10000,
        99999
    )

    return f"autouser{number}"