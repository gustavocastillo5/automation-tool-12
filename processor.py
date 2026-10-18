import time
from typing import Dict, Any, List, Optional


class ClickProcessor:
    """Processes and validates autoclicker action queues inside execution loops."""

    def __init__(self, max_screen_x: int = 3840, max_screen_y: int = 2160):
        self.max_screen_x = max_screen_x
        self.max_screen_y = max_screen_y
        self.is_running = False

    def validate_click_action(self, action: Dict[str, Any]) -> List[str]:
        """Validates input parameters for a single click action before execution."""
        errors = []
        
        x = action.get("x")
        y = action.get("y")
        interval = action.get("interval", 0.1)
        button = action.get("button", "left")

        if x is None or not isinstance(x, int) or not (0 <= x <= self.max_screen_x):
            errors.append(f"invalid X coordinate: {x}")
        if y is None or not isinstance(y, int) or not (0 <= y <= self.max_screen_y):
            errors.append(f"invalid Y coordinate: {y}")
        if not isinstance(interval, (int, float)) or interval < 0.001:
            errors.append(f"invalid click interval: {interval}s (minimum 0.001s)")
        if button not in ("left", "right", "middle"):
            errors.append(f"unsupported mouse button: '{button}'")

        return errors

    def process_loop(self, queue: List[Dict[str, Any]], iterations: int = 1) -> int:
        """Main processing loop that validates and executes queued click events."""
        self.is_running = True
        successful_actions = 0

        for current_iter in range(iterations):
            if not self.is_running:
                break

            for idx, action in enumerate(queue):
                validation_errors = self.validate_click_action(action)
                if validation_errors:
                    error_msg = ", ".join(validation_errors)
                    print(f"[Iteration {current_iter + 1}, Action {idx}] Skipped: {error_msg}")
                    continue

                time.sleep(action.get("interval", 0.1))
                successful_actions += 1

        self.is_running = False
        return successful_actions

    def stop(self) -> None:
        """Stops the processing loop safely."""
        self.is_running = False
