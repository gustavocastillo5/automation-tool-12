import time
import logging

logger = logging.getLogger("autoclicker.processor")

class ActionProcessor:
    """Processes and executes a sequence of simulated mouse and delay events."""

    def __init__(self, safe_mode: bool = True):
        self.safe_mode = safe_mode
        self._running = False

    def execute_sequence(self, actions: list) -> None:
        """Executes a list of actions sequentially with safety checks."""
        self._running = True
        logger.info(f"Starting sequence execution with {len(actions)} actions")

        for index, action in enumerate(actions):
            if not self._running:
                logger.info("Sequence execution aborted by user")
                break

            action_type = action.get("type")
            logger.debug(f"Processing action {index + 1}: {action_type}")

            if action_type == "click":
                self._execute_click(action)
            elif action_type == "delay":
                self._execute_delay(action)
            else:
                logger.warning(f"Unsupported action type encountered: {action_type}")

        self._running = False

    def cancel(self) -> None:
        """Signals the processor to stop running the current sequence."""
        self._running = False

    def _execute_click(self, action: dict) -> None:
        x = action.get("x", 0)
        y = action.get("y", 0)
        clicks = action.get("clicks", 1)
        button = action.get("button", "left")

        logger.info(f"Simulating click: {button} at ({x}, {y}) x{clicks}")
        if not self.safe_mode:
            try:
                import pyautogui
                pyautogui.click(x=x, y=y, clicks=clicks, button=button)
            except ImportError:
                logger.error("pyautogui library missing; click action skipped in active mode")

    def _execute_delay(self, action: dict) -> None:
        duration = action.get("duration", 1.0)
        logger.info(f"Applying delay of {duration} seconds")
        time.sleep(duration)