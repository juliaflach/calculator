from inspect import getmembers, isfunction
from flask import abort, jsonify, request, Response
import calculator as calculator

math_list = [func[0] for func in getmembers(calculator, isfunction)]  # List of operations done by the app

def index() -> Response:
    """
    Return all the operations that can be done by the app.
    """
    return jsonify({'math': math_list})


def get_result() -> Response:
    """
    Return the responses below.
    Responses:
        200: 
            Return the result of the math function in the 'calculator' module that is being called.
        404: 
            The operation is not in the list of operations done by the app.
        500: 
            Could not perform the calculation.
    """
    operation = request.json['operation']
    params = request.json['param']

    if operation not in math_list:
        abort(404, "Invalid operation")

    try: 
        func = getattr(calculator, operation)
        result = func(params)
    except Exception as e: 
        abort(500, f"Calculation error: {e}")
    
    return jsonify({'result': result})
