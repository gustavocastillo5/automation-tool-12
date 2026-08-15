import time
import random

class ClickProcessor:
    def __init__(self, clicks_per_second):
        self.clicks_per_second = clicks_per_second

    def start_clicking(self, duration):
        end_time = time.time() + duration
        while time.time() < end_time:
            self.perform_click()
            time.sleep(1 / self.clicks_per_second)

    def perform_click(self):
        # Simulated click action
        x, y = self.get_random_coordinates()
        print(f'Clicking at ({x}, {y})')  # Replace with actual click action

    def get_random_coordinates(self):
        # Simulate generating random screen coordinates
        x = random.randint(0, 1920)  # Assuming a screen width of 1920
        y = random.randint(0, 1080)  # Assuming a screen height of 1080
        return x, y

if __name__ == '__main__':
    processor = ClickProcessor(clicks_per_second=5)
    processor.start_clicking(duration=10)  # Click for 10 seconds