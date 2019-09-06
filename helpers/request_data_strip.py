def request_data_strip(request_data):
    for key, value in request_data.items():
        if isinstance(value, str):
            request_data[key] = value.strip()

    return request_data
