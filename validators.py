import re

def validate_coordinates(x: int, y: int) -> bool:
    """Checks if coordinates are within standard screen bounds."""
    return 0 <= x <= 10000 and 0 <= y <= 10000

def validate_interval(interval: float) -> bool:
    """Ensures click interval is within safe operational limits."""
    return 0.01 <= interval <= 60.0

def validate_config_data(data: dict) -> bool:
    """Schema verification for autoclicker settings dictionary."""
    required_keys = {'x', 'y', 'interval', 'clicks'}
    if not all(key in data for key in required_keys):
        return False
    
    if not isinstance(data.get('clicks'), int) or data['clicks'] < 0:
        return False
        
    return (
        validate_coordinates(data['x'], data['y']) and 
        validate_interval(data['interval'])
    )

def sanitize_input_string(user_input: str) -> str:
    """Removes non-numeric characters from numeric input fields."""
    return re.sub(r'[^0-9.]', '', user_input)
