import json
import random
from typing import List, Dict, Any

def parse_click_sequence(raw_data: str) -> List[Dict[str, Any]]:
    """Parse raw JSON string containing autoclicker macro actions.
    
    Validates that each action contains x, y coordinates and delay fields.
    """
    try:
        sequence = json.loads(raw_data)
    except json.JSONDecodeError as err:
        raise ValueError(f"Invalid click sequence JSON: {err}")
    
    if not isinstance(sequence, list):
        raise ValueError("Sequence data must be a list of action objects.")
    
    validated_actions = []
    for index, action in enumerate(sequence):
        if not isinstance(action, dict):
            raise ValueError(f"Action at index {index} is not a valid dictionary.")
        
        x = action.get("x")
        y = action.get("y")
        delay = action.get("delay", 0.1)
        button = action.get("button", "left")

        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise ValueError(f"Action at index {index} contains invalid coordinates.")
        
        validated_actions.append({
            "x": int(x),
            "y": int(y),
            "delay": max(0.001, float(delay)),
            "button": str(button).lower()
        })
        
    return validated_actions

def apply_delay_jitter(base_delay: float, jitter_percentage: float = 0.1) -> float:
    """Calculate a humanized delay by applying random jitter to a base interval."""
    jitter_percentage = max(0.0, min(1.0, jitter_percentage))
    variation = base_delay * jitter_percentage
    actual_delay = base_delay + random.uniform(-variation, variation)
    return max(0.001, round(actual_delay, 4))
