import time
import pyautogui
from threading import Event

class AutoClicker:
    """Core engine for automating mouse click sequences."""
    def __init__(self, interval=0.1, stop_event=None):
        self.interval = interval
        self.stop_event = stop_event or Event()

    def run(self):
        """Executes clicks until stop signal is received."""
        try:
            while not self.stop_event.is_set():
                pyautogui.click()
                time.sleep(self.interval)
        except pyautogui.FailSafeException:
            print("Safety trigger activated, stopping clicker.")

def initialize_session(config):
    """Factory method to prepare clicker instance."""
    stop_signal = Event()
    engine = AutoClicker(
        interval=config.get('delay', 0.5),
        stop_event=stop_signal
    )
    return engine, stop_signal

if __name__ == "__main__":
    # Demo execution block
    clicker, signal = initialize_session({'delay': 1.0})
    print("Starting automation in 3 seconds...")
    time.sleep(3)
    clicker.run()