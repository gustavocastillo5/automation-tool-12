import time
from typing import Dict, Any, List

class ClickHandler:
    """Handles and validates autoclicker tasks in the main execution loop."""

    def __init__(self, max_screen_width: int = 1920, max_screen_height: int = 1080):
        self.max_width = max_screen_width
        self.max_height = max_screen_height
        self.allowed_buttons = {"left", "right", "middle"}

    def validate_task(self, task: Dict[str, Any]) -> bool:
        """Validates click payload parameters before execution."""
        x = task.get("x")
        y = task.get("y")
        if not isinstance(x, int) or not isinstance(y, int):
            print("[Warning] Task rejected: Coordinates must be integers.")
            return False
        if not (0 <= x <= self.max_width and 0 <= y <= self.max_height):
            print(f"[Warning] Invalid coordinates: ({x}, {y}) out of bounds.")
            return False

        interval = task.get("interval", 0.1)
        if not isinstance(interval, (int, float)) or interval <= 0:
            print(f"[Warning] Invalid click interval: {interval}. Must be > 0.")
            return False

        clicks = task.get("clicks", 1)
        if not isinstance(clicks, int) or clicks < 1:
            print(f"[Warning] Invalid click count: {clicks}. Must be >= 1.")
            return False

        button = task.get("button", "left")
        if button not in self.allowed_buttons:
            print(f"[Warning] Invalid button type: '{button}'.")
            return False

        return True

    def process_queue(self, task_queue: List[Dict[str, Any]]) -> int:
        """Main processing loop that validates and executes autoclicker commands."""
        successful_executed = 0

        for index, task in enumerate(task_queue):
            print(f"Processing task {index + 1}/{len(task_queue)}...")

            if not isinstance(task, dict) or not self.validate_task(task):
                print(f"Skipping task {index + 1} due to validation failure.")
                continue

            x, y = task["x"], task["y"]
            interval = task.get("interval", 0.1)
            button = task.get("button", "left")
            clicks = task.get("clicks", 1)

            print(f"Executing: {clicks} {button}-click(s) at ({x}, {y}) with {interval}s delay.")
            time.sleep(0.01)
            successful_executed += 1

        return successful_executed