def success_response(data=None, message=None, status_code=200):
    response = {"success": True}

    if message:
        response["message"] = message
    if data is not None:
        response["data"] = data

    return response, status_code


def error_response(message, status_code=400):
    return {
        "success": False,
        "error": message
    }, status_code
