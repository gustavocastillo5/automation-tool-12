import time
import threading

# Handler for managing autoclick operations in the tool
class ClickHandler:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.active = False
        self.thread = None
        self.stop_flag = threading.Event()

    def initiate_clicking(self):
        # Start if not already active
        if self.active:
            return
        self.active = True
        self.stop_flag.clear()
        self.thread = threading.Thread(target=self._clicking_routine)
        self.thread.daemon = True
        self.thread.start()

    def terminate_clicking(self):
        # Stop the process cleanly
        if not self.active:
            return
        self.active = False
        self.stop_flag.set()
        if self.thread is not None:
            self.thread.join(timeout=1.0)

    def _clicking_routine(self):
        # Main loop reorganized for clarity
        while not self.stop_flag.is_set():
            self._do_click_action()
            time.sleep(self.interval)

    def _do_click_action(self):
        # Simulated for this environment
        print("Simulated click performed.")

    def update_interval(self, new_interval):
        # Validate and set new interval
        if new_interval > 0:
            self.interval = new_interval

if __name__ == "__main__":
    handler = ClickHandler(0.2)
    handler.initiate_clicking()
    time.sleep(2)
    handler.terminate_clicking()