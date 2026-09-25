import time
import logging
from typing import Dict, Any, Tuple

logger = logging.getLogger(__name__)


class ScreenBoundsError(Exception):
    """Raised when target coordinates fall outside display area."""
    pass


class InvalidActionError(Exception):
    """Raised when an unsupported macro action is provided."""
    pass


class ActionProcessor:
    def __init__(self, screen_size: Tuple[int, int] = (1920, 1080)):
        self.screen_width, self.screen_height = screen_size
        self.allowed_actions = {"click", "double_click", "right_click", "hold"}

    def validate_coordinates(self, x: int, y: int) -> None:
        """Verify target coordinates are within monitor bounds."""
        if not (0 <= x <= self.screen_width and 0 <= y <= self.screen_height):
            raise ScreenBoundsError(f"Target ({x}, {y}) outside bounds ({self.screen_width}x{self.screen_height})")

    def process(self, action: Dict[str, Any]) -> bool:
        """Process automated click action with robust edge case checks."""
        if not isinstance(action, dict):
            logger.error("Action payload must be a valid dictionary")
            return False

        action_type = action.get("type", "click")
        delay = action.get("delay", 0.0)

        try:
            if action_type not in self.allowed_actions:
                raise InvalidActionError(f"Unsupported action: '{action_type}'")

            x, y = action.get("x"), action.get("y")
            if x is None or y is None:
                raise ValueError("Action requires valid 'x' and 'y' coordinates")

            self.validate_coordinates(int(x), int(y))

            # Handle negative delay edge cases
            safe_delay = max(0.0, float(delay))
            if safe_delay != delay:
                logger.warning(f"Normalized negative delay {delay}s to 0.0s")

            time.sleep(safe_delay)
            logger.info(f"Successfully processed {action_type} at ({x}, {y})")
            return True

        except (ScreenBoundsError, InvalidActionError, ValueError) as err:
            logger.error(f"Validation failure: {err}")
            return False
        except Exception as err:
            logger.critical(f"Unexpected error executing macro action: {err}")
            return False
