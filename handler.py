import time
from typing import Optional

class ClickHandler:
    """
    A class to manage automated click actions.
    """

    def __init__(self, interval: float):
        """
        Initializes the ClickHandler with a specified interval.
        
        :param interval: Time in seconds between clicks
        """
        self.interval = interval
        self.running = False

    def start_clicking(self) -> None:
        """
        Starts the clicking process.
        
        This method runs an infinite loop, clicking at the specified interval.
        """
        self.running = True
        while self.running:
            self.click()
            time.sleep(self.interval)

    def stop_clicking(self) -> None:
        """
        Stops the clicking process.
        """
        self.running = False

    def click(self) -> None:
        """
        Simulates a mouse click action.
        
        This method would contain the actual clicking logic.
        """
        print("Click")  # Replace with actual clicking code

if __name__ == '__main__':
    handler = ClickHandler(interval=1.0)
    try:
        handler.start_clicking()
    except KeyboardInterrupt:
        handler.stop_clicking()  # Safely stop clicking on interrupt
