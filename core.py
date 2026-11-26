import time
import pyautogui

def run_autoclicker(interval, count):
    """Executes mouse clicks based on validated user input."""
    print(f"Starting autoclicker: {count} clicks with {interval}s interval.")
    
    for i in range(count):
        pyautogui.click()
        time.sleep(interval)
        print(f"Click {i + 1}/{count} completed.")

def main():
    try:
        user_interval = input("Enter interval (seconds): ")
        user_count = input("Enter click count: ")

        # Validation logic for input parameters
        interval = float(user_interval)
        count = int(user_count)

        if interval < 0.1:
            raise ValueError("Interval must be at least 0.1 seconds.")
        if count <= 0:
            raise ValueError("Click count must be a positive integer.")

        run_autoclicker(interval, count)

    except ValueError as e:
        print(f"Input validation error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

if __name__ == "__main__":
    main()