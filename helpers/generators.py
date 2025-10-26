import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def generate_order_payload(color=["BLACK", "GREY"]):

    first_name = f"User_{generate_random_string(6)}"
    last_name = f"Test_{generate_random_string(6)}"
    address = f"{generate_random_string(8)} str, bld {random.randint(1, 50)}, apt {random.randint(1, 100)}"
    metro_station = random.randint(1, 237)
    phone = f"+7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"
    rent_time = random.randint(1, 5)
    delivery_date = f"2025-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    comment = f"Test order {generate_random_string(8)}"   
    color = color
    payload = {
        "firstName": first_name,
        "lastName": last_name,
        "address": address,
        "metroStation": metro_station,
        "phone": phone,
        "rentTime": rent_time,
        "deliveryDate": delivery_date,
        "comment": comment,
        "color": color
    }

    return payload
