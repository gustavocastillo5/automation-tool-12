import time
from typing import Dict, Any, List, Tuple

class CommandHandler:
    def __init__(self, screen_width: int = 1920, screen_height: int = 1080):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.valid_buttons = {"left", "right", "middle"}

    def validate_click_event(self, payload: Dict[str, Any]) -> Tuple[bool, str]:
        """Validate click payload attributes before execution."""
        x = payload.get("x")
        y = payload.get("y")
        button = payload.get("button", "left")
        interval = payload.get("interval", 0.1)
        repeat = payload.get("repeat", 1)

        if not isinstance(x, int) or not (0 <= x <= self.screen_width):
            return False, f"Invalid X coordinate: {x}. Must be 0-{self.screen_width}."
        
        if not isinstance(y, int) or not (0 <= y <= self.screen_height):
            return False, f"Invalid Y coordinate: {y}. Must be 0-{self.screen_height}."
        
        if button not in self.valid_buttons:
            return False, f"Invalid mouse button: {button}. Allowed: {self.valid_buttons}."
        
        if not isinstance(interval, (int, float)) or interval < 0.01:
            return False, f"Invalid interval: {interval}. Minimum is 0.01 seconds."

        if not isinstance(repeat, int) or repeat < 1:
            return False, f"Invalid repeat count: {repeat}. Must be >= 1."

        return True, "Valid payload"

    def process_queue(self, queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Main processing loop for incoming click commands with strict validation."""
        processed_results = []
        for index, item in enumerate(queue):
            is_valid, message = self.validate_click_event(item)
            if not is_valid:
                processed_results.append({"status": "rejected", "reason": message, "index": index})
                continue
            
            processed_results.append({
                "status": "accepted",
                "index": index,
                "action": f"Clicked {item['button']} at ({item['x']}, {item['y']})"
            })
        return processed_results