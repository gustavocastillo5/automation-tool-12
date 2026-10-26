import time
import pyautogui

def run_autoclicker(interval: float, clicks: int):
    """Executes clicks based on validated user input."""
    if not isinstance(interval, (int, float)) or interval < 0:
        raise ValueError("Interval must be a non-negative number")
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError("Click count must be a positive integer")

    print(f"Starting automation: {clicks} clicks at {interval}s intervals")
    
    try:
        for i in range(clicks):
            pyautogui.click()
            time.sleep(interval)
            print(f"Click {i+1}/{clicks} complete")
    except pyautogui.FailSafeException:
        print("Fail-safe triggered: aborting execution")

def main():
    # Example inputs for the automation processing loop
    try:
        user_interval = float(input("Enter interval (seconds): "))
        user_clicks = int(input("Enter number of clicks: "))
        
        run_autoclicker(user_interval, user_clicks)
    except ValueError as e:
        print(f"Input validation error: {e}")

if __name__ == "__main__":
    main()