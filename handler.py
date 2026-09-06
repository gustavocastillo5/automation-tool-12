import time
import threading
from typing import Callable, Optional

class ClickHandler:
    """Manages the background thread execution for the autoclicker.

    This class handles starting, stopping, and running the autoclick loop
    with safety checks, a configurable interval, and custom execution actions.
    """

    def __init__(self, click_action: Callable[[], None], interval: float = 0.1) -> None:
        """Initializes the click handler with an action and interval.

        Args:
            click_action: A parameterless function executed on every click.
            interval: Time in seconds to sleep between consecutive clicks.
        """
        self.click_action: Callable[[], None] = click_action
        self.interval: float = interval
        self._running: bool = False
        self._thread: Optional[threading.Thread] = None

    def _loop(self) -> None:
        """Internal execution loop running on a dedicated worker thread."""
        while self._running:
            try:
                self.click_action()
            except Exception:
                self._running = False
                break
            time.sleep(self.interval)

    def start(self) -> bool:
        """Starts the autoclicking loop in a separate thread.

        Returns:
            bool: True if successfully started, False if already running.
        """
        if self._running:
            return False

        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        return True

    def stop(self) -> bool:
        """Stops the autoclicking loop.

        Returns:
            bool: True if successfully stopped, False if it was not running.
        """
        if not self._running:
            return False

        self._running = False
        if self._thread is not None:
            self._thread.join(timeout=1.0)
            self._thread = None
        return True

    @property
    def is_active(self) -> bool:
        """Checks if the click loop is currently running.

        Returns:
            bool: Current execution state.
        """
        return self._running