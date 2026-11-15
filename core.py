import time
import threading
from typing import Callable, Optional
from enum import Enum, auto


class ClickButton(Enum):
    """Enumeration of supported mouse buttons for click events."""
    LEFT = auto()
    RIGHT = auto()
    MIDDLE = auto()


class AutoClicker:
    """Core automation engine for managing background mouse clicking tasks."""

    def __init__(self, interval: float = 0.1, button: ClickButton = ClickButton.LEFT) -> None:
        """Initialize the autoclicker with click delay and target button.
        
        Args:
            interval: Time delay between clicks in seconds.
            button: Target mouse button to trigger.
        """
        self.interval: float = max(0.001, interval)
        self.button: ClickButton = button
        self.running: bool = False
        self.click_count: int = 0
        self._thread: Optional[threading.Thread] = None
        self._click_handler: Optional[Callable[[ClickButton], None]] = None

    def set_handler(self, handler: Callable[[ClickButton], None]) -> None:
        """Register a custom callback handler for mouse click execution."""
        self._click_handler = handler

    def _run_loop(self) -> None:
        """Execute repetitive clicking in dedicated background thread loop."""
        while self.running:
            if self._click_handler:
                self._click_handler(self.button)
            self.click_count += 1
            time.sleep(self.interval)

    def start(self) -> bool:
        """Start the autoclicker execution thread if currently inactive."""
        if self.running:
            return False
        self.running = True
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()
        return True

    def stop(self) -> int:
        """Halt click thread execution and return total performed clicks."""
        if not self.running:
            return self.click_count
        self.running = False
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        return self.click_count
