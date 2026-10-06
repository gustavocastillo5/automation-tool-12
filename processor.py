import logging
import time
from typing import Dict, List, Tuple, Union

logger = logging.getLogger("autoclicker.processor")


class ScreenBoundsError(ValueError):
    """Raised when coordinates fall outside allowed physical or safety bounds."""
    pass


class ClickProcessor:
    """Manages the validation and safe execution of automated clicks."""

    def __init__(self, screen_resolution: Tuple[int, int], safety_margin: int = 10):
        self.width, self.height = screen_resolution
        self.safety_margin = safety_margin
        self.is_running = False

    def validate_coordinates(self, x: int, y: int) -> bool:
        """Validates if coordinates are within safe screen boundaries."""
        if x < self.safety_margin or x > (self.width - self.safety_margin):
            return False
        if y < self.safety_margin or y > (self.height - self.safety_margin):
            return False
        if x <= self.safety_margin and y <= self.safety_margin:
            return False
        return True

    def process_click_queue(
        self, clicks: List[Tuple[int, int, float]]
    ) -> Dict[str, Union[int, List[str]]]:
        """Processes a queue of clicks with safe boundary checks and delays."""
        self.is_running = True
        processed_count = 0
        errors = []

        for index, click_event in enumerate(clicks):
            if not self.is_running:
                logger.info("Processing halted by safety event.")
                break

            try:
                if len(click_event) != 3:
                    raise ValueError(
                        f"Malformed click data at index {index}. Expected (x, y, delay)."
                    )

                x, y, delay = click_event

                if not self.validate_coordinates(x, y):
                    raise ScreenBoundsError(
                        f"Click coordinate ({x}, {y}) violates safety margins."
                    )

                if delay < 0.0:
                    raise ValueError(f"Negative delay {delay}s is not permitted.")

                logger.debug(f"Executing simulated click at ({x}, {y})")
                time.sleep(delay)
                processed_count += 1

            except (ScreenBoundsError, ValueError) as err:
                error_msg = f"Event {index} skipped: {str(err)}"
                logger.error(error_msg)
                errors.append(error_msg)
            except Exception as unexpected_err:
                error_msg = f"Unexpected system error at event {index}: {str(unexpected_err)}"
                logger.critical(error_msg)
                errors.append(error_msg)
                self.is_running = False

        self.is_running = False
        return {"processed": processed_count, "errors": errors}