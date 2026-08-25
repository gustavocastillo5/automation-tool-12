import time

# Validation functions for autoclicker inputs
def is_valid_coordinate(x, y):
    if not isinstance(x, int) or not isinstance(y, int):
        return False
    if x < 0 or x > 1920 or y < 0 or y > 1080:
        return False
    return True

def is_valid_interval(interval):
    if not isinstance(interval, (int, float)) or interval <= 0 or interval > 3600:
        return False
    return True

def is_valid_click_count(count):
    if not isinstance(count, int) or count <= 0 or count > 1000:
        return False
    return True

def run_autoclicker():
    test_cases = [
        (100, 200, 0.5, 3),
        (-10, 300, 2, 5),
        (500, 400, 0, 3),
        (800, 600, 1, -1),
        (1200, 900, 3, 20),
    ]
    # Main processing loop with input validation
    for x, y, interval, click_count in test_cases:
        if not is_valid_coordinate(x, y):
            print(f"Invalid coordinates: ({x}, {y}). Skipping.")
            continue
        if not is_valid_interval(interval):
            print(f"Invalid interval: {interval}. Skipping.")
            continue
        if not is_valid_click_count(click_count):
            print(f"Invalid click count: {click_count}. Skipping.")
            continue
        print(f"Processing: click at ({x}, {y}) every {interval}s, {click_count} times")
        for i in range(click_count):
            print(f"  Simulated click {i+1}")
            time.sleep(interval)
    print("Processing completed.")

if __name__ == "__main__":
    run_autoclicker()