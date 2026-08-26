import time
from typing import Optional, Dict, Any

class ClickProcessor:
    """Handles the execution logic and timing for the autoclicker."""

    def __init__(self, delay: float = 0.1, max_clicks: Optional[int] = None) -> None:
        """Initialize the processor with delay and click limit."""
        self.delay: float = delay
        self.max_clicks: Optional[int] = max_clicks
        self.click_count: int = 0
        self.is_running: bool = False

    def process_click_cycle(self) -> Dict[str, Any]:
        """Execute a single click cycle and return status information."""
        if self.max_clicks is not None and self.click_count >= self.max_clicks:
            self.is_running = False
            return {"status": "limit_reached", "clicks": self.click_count}

        # Simulate click action delay
        time.sleep(self.delay)
        self.click_count += 1
        
        return {
            "status": "success",
            "clicks": self.click_count,
            "delay": self.delay
        }

    def reset(self) -> None:
        """Reset the click counter and running state."""
        self.click_count = 0
        self.is_running = False
