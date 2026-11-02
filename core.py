import time
from typing import Dict, Any, List, Optional

class ClickConfigError(ValueError):
    """Raised when autoclicker input parameters fail validation."""
    pass

def validate_click_params(params: Dict[str, Any]) -> Dict[str, Any]:
    """Validate click configuration dictionary parameters."""
    interval = params.get("interval", 0.1)
    if not isinstance(interval, (int, float)) or interval <= 0:
        raise ClickConfigError(f"Invalid interval: {interval}. Must be positive number.")

    clicks = params.get("clicks", 1)
    if not isinstance(clicks, int) or clicks < 0:
        raise ClickConfigError(f"Invalid click count: {clicks}. Must be non-negative integer.")

    button = params.get("button", "left")
    if button not in ("left", "right", "middle"):
        raise ClickConfigError(f"Invalid button type: '{button}'. Must be left, right, or middle.")

    position = params.get("position")
    if position is not None:
        if not (isinstance(position, (tuple, list)) and len(position) == 2):
            raise ClickConfigError(f"Invalid position format: {position}. Must be (x, y).")
        if not all(isinstance(c, int) and c >= 0 for c in position):
            raise ClickConfigError(f"Invalid coordinates: {position}. Must be non-negative integers.")

    return {
        "interval": float(interval),
        "clicks": int(clicks),
        "button": button,
        "position": position
    }

def process_autoclick_queue(queue: List[Dict[str, Any]]) -> Dict[str, int]:
    """Main processing loop that validates input configs and executes clicks."""
    stats = {"processed": 0, "failed": 0, "total_clicks": 0}

    for item in queue:
        try:
            # Validate input parameters before execution
            valid_config = validate_click_params(item)
            
            # Execute simulated click sequence
            click_count = valid_config["clicks"]
            interval = valid_config["interval"]
            
            for _ in range(click_count):
                time.sleep(min(interval, 0.01))
                stats["total_clicks"] += 1
            
            stats["processed"] += 1
        except ClickConfigError:
            # Skip invalid configs safely without crashing the main loop
            stats["failed"] += 1

    return stats