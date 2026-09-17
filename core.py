import pyautogui
import time
import threading

class AutoClicker:
    """Handles click automation cycles"""
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False

    def start_clicking(self):
        """Executes primary click loop"""
        self.running = True
        while self.running:
            pyautogui.click()
            time.sleep(self.interval)

    def stop_clicking(self):
        """Terminates execution"""
        self.running = False

    def run_in_thread(self):
        """Spawns worker thread"""
        thread = threading.Thread(target=self.start_clicking)
        thread.daemon = True
        thread.start()

if __name__ == '__main__':
    clicker = AutoClicker(interval=0.5)
    print('Starting automation. Press Ctrl+C to stop.')
    try:
        clicker.run_in_thread()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        clicker.stop_clicking()
        print('Automation stopped.')