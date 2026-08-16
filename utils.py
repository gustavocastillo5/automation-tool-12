import time
import threading

class RateLimiter:
    def __init__(self, rate_limit):
        self.rate_limit = rate_limit  # max calls per second
        self.last_called = 0.0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            current_time = time.time()
            elapsed = current_time - self.last_called
            wait_time = max(0, (1 / self.rate_limit) - elapsed)
            if wait_time > 0:
                time.sleep(wait_time)
            self.last_called = time.time()

def autoclick(click_action, rate_limit):
    limiter = RateLimiter(rate_limit)
    while True:
        limiter.wait()  # control the click rate
        click_action()  # perform the click

# Example usage
if __name__ == '__main__':
    def click_action():
        print('Click!')

    autoclick(click_action, 5)  # 5 clicks per second
