def validate_json(data, required_fields):
   
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise AssertionError(f"Missing required fields: {missing_fields}")   

    return True

def validate_order_response(response_data):
    """
    валидация для ответа с заказом
    """

    required_fields = ["order"]
    validate_json(response_data, required_fields)
    order_required_fields = [
        "id", "firstName", "lastName", "address", "metroStation",
        "phone", "rentTime", "deliveryDate", "track", "status", "color"
    ]
    validate_json(response_data["order"], order_required_fields)
    
    return True
