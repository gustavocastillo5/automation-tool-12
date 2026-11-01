import time
from typing import Dict, Any, Optional

class AutoClicker:
    VALID_BUTTONS = {"left", "right", "middle"}

    def __init__(self):
        self.is_running = False

    def validate_task_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validates click execution parameters before starting the process loop."""
        interval = config.get("interval")
        if not isinstance(interval, (int, float)) or interval <= 0:
            raise ValueError(f"Invalid interval '{interval}': must be a positive number.")

        clicks = config.get("clicks", 0)
        if not isinstance(clicks, int) or clicks < 0:
            raise ValueError(f"Invalid clicks count '{clicks}': must be an integer >= 0.")

        button = str(config.get("button", "left")).lower()
        if button not in self.VALID_BUTTONS:
            raise ValueError(f"Invalid mouse button '{button}': must be one of {self.VALID_BUTTONS}.")

        coords = config.get("coordinates")
        if coords is not None:
            if not isinstance(coords, tuple) or len(coords) != 2:
                raise ValueError("Coordinates must be a tuple of (x, y).")
            x, y = coords
            if not (isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0):
                raise ValueError("Coordinate values x and y must be non-negative integers.")

        return {
            "interval": float(interval),
            "clicks": clicks,
            "button": button,
            "coordinates": coords
        }

    def execute_click_loop(self, task_config: Dict[str, Any]) -> int:
        """Main processing loop executing validated auto-click tasks."""
        validated = self.validate_task_config(task_config)
        self.is_running = True
        performed_clicks = 0

        print(f"Starting clicker: interval={validated['interval']}s, button={validated['button']}.")

        try:
            while self.is_running:
                if validated["clicks"] > 0 and performed_clicks >= validated["clicks"]:
                    print("Target click count reached. Stopping processing loop.")
                    break

                target = validated["coordinates"] or "current position"
                print(f"[{performed_clicks + 1}] Clicked '{validated['button']}' at {target}")
                performed_clicks += 1

                time.sleep(validated["interval"])
        finally:
            self.is_running = False

        return performed_clicks
