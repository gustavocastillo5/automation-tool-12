import time
import logging

# Configure logger for output monitoring
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class ClickActionHandler:
    """Handles the validation and execution of autoclicker coordinate cues."""
    
    MAX_SCREEN_WIDTH = 7680
    MAX_SCREEN_HEIGHT = 4320
    VALID_BUTTONS = {"left", "right", "middle"}

    def __init__(self, actions: list):
        self.actions = actions
        self.is_running = False

    def validate_action(self, action: dict) -> bool:
        """Validates individual action configuration boundaries before execution."""
        try:
            x = action.get("x")
            y = action.get("y")
            button = action.get("button", "left")
            delay = action.get("delay", 0.1)
            repeats = action.get("repeats", 1)

            if not isinstance(x, int) or not (0 <= x <= self.MAX_SCREEN_WIDTH):
                logging.error(f"Invalid X coordinate: {x}. Must be 0-{self.MAX_SCREEN_WIDTH}")
                return False
            if not isinstance(y, int) or not (0 <= y <= self.MAX_SCREEN_HEIGHT):
                logging.error(f"Invalid Y coordinate: {y}. Must be 0-{self.MAX_SCREEN_HEIGHT}")
                return False
            if button not in self.VALID_BUTTONS:
                logging.error(f"Invalid button: {button}. Must be {self.VALID_BUTTONS}")
                return False
            if not isinstance(delay, (int, float)) or delay < 0:
                logging.error(f"Invalid delay: {delay}. Must be positive number")
                return False
            if not isinstance(repeats, int) or repeats <= 0:
                logging.error(f"Invalid repeat count: {repeats}. Must be greater than 0")
                return False

            return True
        except Exception as e:
            logging.error(f"Action parsing failure: {e}")
            return False

    def start_loop(self):
        """Executes the queue while validating inputs dynamic in the loop."""
        self.is_running = True
        logging.info("Initializing handler processing loop...")

        for index, action in enumerate(self.actions):
            if not self.is_running:
                break

            logging.info(f"Evaluating action item {index + 1}...")
            if not self.validate_action(action):
                logging.warning(f"Skipping step {index + 1} due to failed input checks")
                continue

            # Simulate the click sequence safely post-validation
            for _ in range(action.get("repeats", 1)):
                time.sleep(action.get("delay", 0.1))
                logging.info(f"Simulated {action['button']} click at ({action['x']}, {action['y']})")

        self.is_running = False
        logging.info("Loop execution cycle finished")