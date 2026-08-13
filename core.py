import time
import threading

class AutoClicker:
    def __init__(self, interval: float):
        self.interval = interval
        self.running = False
        self.thread = None

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._click_loop)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread:
            self.thread.join()
            self.thread = None

    def _click_loop(self):
        while self.running:
            self._perform_click()
            time.sleep(self.interval)

    def _perform_click(self):
        # Replace with actual click logic
        print('Click!')

if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.1)
    try:
        autoclicker.start()
        time.sleep(2)  # Run for 2 seconds
    finally:
        autoclicker.stop()