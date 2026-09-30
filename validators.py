def validate_click_parameters(interval, count):
    """
    Validates input parameters for the autoclicker logic.
    Ensures interval is positive and count is non-negative.
    """
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ValueError(f"Interval must be a positive number, got: {interval}")
    
    if not isinstance(count, int) or count < 0:
        raise ValueError(f"Count must be a non-negative integer, got: {count}")

    return True

def validate_coordinate(x, y):
    """
    Checks if coordinates are valid screen integers.
    """
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError("Coordinates must be integers")
    
    if x < 0 or y < 0:
        raise ValueError("Coordinates cannot be negative")
        
    return True

def validate_input_schema(data):
    """
    General schema validation for configuration dictionary.
    """
    required_keys = {'interval', 'count', 'x', 'y'}
    if not all(key in data for key in required_keys):
        raise KeyError(f"Missing required keys: {required_keys - data.keys()}")
    
    validate_click_parameters(data['interval'], data['count'])
    validate_coordinate(data['x'], data['y'])
    
    return True