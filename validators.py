import logging

def validate_click_params(interval: float, iterations: int) -> bool:
    """
    Validates input parameters for the automation loop.
    Ensures click interval is positive and iterations are non-negative.
    """
    logger = logging.getLogger("automation-tool-12")
    
    if not isinstance(interval, (int, float)) or interval <= 0:
        logger.error(f"Invalid interval: {interval}. Must be a positive number.")
        return False
        
    if not isinstance(iterations, int) or iterations < 0:
        logger.error(f"Invalid iterations: {iterations}. Must be 0 (infinite) or greater.")
        return False
        
    return True

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """
    Validates if coordinates are within the screen boundaries.
    """
    if 0 <= x <= screen_width and 0 <= y <= screen_height:
        return True
    
    logging.warning(f"Coordinates ({x}, {y}) outside screen bounds ({screen_width}x{screen_height}).")
    return False
