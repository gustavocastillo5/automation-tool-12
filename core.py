import time

class AutoClicker:
    def __init__(self, click_interval=1.0):
        self.click_interval = click_interval
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.click()
            time.sleep(self.click_interval)

    def stop(self):
        self.running = False

    def click(self):
        # Simulate a mouse click
        print('Mouse clicked!')  # Replace with actual click logic

    def set_interval(self, interval):
        # Performance optimization: avoid redundant updates
        if interval > 0:
            self.click_interval = interval

if __name__ == '__main__':
    autoclicker = AutoClicker(0.5)  # Set default click interval
    try:
        autoclicker.start()  # Start autoclicking
    except KeyboardInterrupt:
        autoclicker.stop()  # Stop on keyboard interrupt
