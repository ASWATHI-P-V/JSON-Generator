from rest_framework.response import Response
from rest_framework import status

def api_response(success, message=None, data=None, status_code=status.HTTP_200_OK, headers=None):
    """
    Generates a consistent API response.
    If it's a 400 Bad Request due to validation errors, it sets the 'message'
    to the specific error and sets 'data' to null.
    The headers argument will be passed directly to rest_framework.response.Response.
    """
    response_data = {}
    response_data["success"] = success

    if not success and status_code == status.HTTP_400_BAD_REQUEST:
        # If 'data' is a dictionary, try to extract a specific message.
        # This is where we ensure the specific validation error message is used.
        if isinstance(data, dict) and data: # Ensure data is a non-empty dict
            # If the serializer passed a message already (e.g., from an APIException)
            # or if it's a ValidationError with a specific field error
            if message: # Prioritize an explicit message if provided
                response_data["message"] = message
            else: # Otherwise, extract from the validation errors
                response_data["message"] = _extract_single_error_message(data)
            response_data["data"] = None
        else: # Fallback for other 400 cases or if data is not a dict
            response_data["message"] = message if message is not None else "Invalid request data."
            response_data["data"] = None
    else:
        response_data["message"] = message if message is not None else ("Operation successful." if success else "An error occurred.")
        response_data["data"] = data

    return Response(response_data, status=status_code, headers=headers)
