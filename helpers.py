import logging

def validate_click_params(interval: float, iterations: int) -> bool:
    """Validate autoclicker parameters to prevent invalid inputs."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.01:
            logging.error(f"Invalid interval: {interval}. Must be >= 0.01.")
            return False
        
        if not isinstance(iterations, int) or iterations < -1:
            logging.error(f"Invalid iteration count: {iterations}. Must be >= -1.")
            return False
            
        return True
    except Exception as e:
        logging.error(f"Validation error occurred: {e}")
        return False

def sanitize_input(value: str) -> float:
    """Convert string input to safe float representation."""
    try:
        cleaned = float(value.strip())
        return max(0.01, cleaned)
    except (ValueError, TypeError):
        logging.warning("Failed to sanitize input, defaulting to 0.1s")
        return 0.1

def validate_coordinates(x: int, y: int) -> bool:
    """Ensure mouse coordinates are within reasonable bounds."""
    if not all(isinstance(val, int) for val in (x, y)):
        return False
    return x >= 0 and y >= 0