import logging

def validate_click_settings(interval: float, iterations: int) -> bool:
    """Ensures click settings are within operational safety bounds."""
    logger = logging.getLogger('automation-tool-12')
    
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f"Invalid interval: {interval}. Must be >= 0.01 seconds.")
        return False
        
    if not isinstance(iterations, int) or iterations < -1:
        logger.error(f"Invalid iterations: {iterations}. Must be -1 (infinite) or >= 1.")
        return False
        
    return True

def validate_coordinate(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if target coordinates are within screen boundaries."""
    logger = logging.getLogger('automation-tool-12')
    
    if 0 <= x <= screen_width and 0 <= y <= screen_height:
        return True
        
    logger.error(f"Coordinates ({x}, {y}) out of bounds ({screen_width}x{screen_height}).")
    return False

def sanitize_input_config(config: dict) -> dict:
    """Filters and sanitizes configuration dictionary keys."""
    allowed_keys = {'interval', 'iterations', 'x', 'y'}
    return {k: v for k, v in config.items() if k in allowed_keys}