from faker import Faker

faker = Faker()

def make_customer():
    first = faker.first_name()
    last = faker.last_name()
    email = faker.email(domain="example.test")
    password = faker.password(length=12) + "9!"
    return {
        "first": first,
        "last": last,
        "email": email,
        "password": password,
        "address": {
            "alias": "Home",
            "company": faker.company(),
            "address1": faker.street_address(),
            "city": faker.city(),
            "postcode": faker.postcode(),
            "phone": faker.msisdn(),
            "country": "United Kingdom"
        }
    }
