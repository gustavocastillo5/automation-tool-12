import time

class AutoClicker:
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.click()
            time.sleep(self.interval)

    def stop(self):
        self.running = False

    def click(self):
        # Simulating mouse click
        print('Mouse clicked!')  # Replace with actual click logic

    def set_interval(self, interval):
        self.interval = interval

    def adjust_speed(self, new_speed):
        if self.running:  # Only adjust if running
            self.stop()  # Stop before adjusting
            self.set_interval(new_speed)
            self.start()  # Restart with new speed

# Example usage
if __name__ == '__main__':
    autoclicker = AutoClicker(interval=0.2)
    try:
        autoclicker.start()
    except KeyboardInterrupt:
        autoclicker.stop()