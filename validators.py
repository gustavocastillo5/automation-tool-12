def validate_click_params(clicks: int, interval: float) -> bool:
    """
    validates input parameters for the autoclicker loop
    returns true if parameters are within operational bounds
    """
    try:
        if not isinstance(clicks, int) or clicks <= 0:
            return False
        if not isinstance(interval, (int, float)) or interval < 0.01:
            return False
        return True
    except (TypeError, ValueError):
        return False

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple[int, int]:
    """
    ensures click coordinates remain within active monitor boundaries
    returns clamped (x, y) coordinates
    """
    valid_x = max(0, min(x, screen_width))
    valid_y = max(0, min(y, screen_height))
    return (valid_x, valid_y)

def validate_user_input(user_data: dict) -> bool:
    """
    full schema validation for automation tool input settings
    """
    required_keys = {'clicks', 'interval', 'x', 'y'}
    if not all(key in user_data for key in required_keys):
        return False
    
    return validate_click_params(user_data['clicks'], user_data['interval'])
