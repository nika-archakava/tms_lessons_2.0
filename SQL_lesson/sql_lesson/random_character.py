from faker import Faker


def create_random_character():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    blood_status = fake.random_element(elements=('Pure-blood', 'Half-blood', 'Muggle-born', 'Half-breed'))
    birth_year = fake.random_int(min=1900, max=2000)
    random_character = (first_name, last_name, blood_status, birth_year)
    return random_character
