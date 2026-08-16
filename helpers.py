import time
import random

def validate_input(input_value):
    if not isinstance(input_value, (int, float)):
        raise ValueError('Input must be a number.')
    if input_value < 0:
        raise ValueError('Input must be non-negative.')
    return True

def perform_click(delay):
    time.sleep(delay)
    print(f'Click performed after {delay} seconds.')

def main_loop():
    while True:
        try:
            user_input = float(input('Enter click delay in seconds (0 to exit): '))
            if user_input == 0:
                print('Exiting...')
                break
            validate_input(user_input)
            perform_click(user_input)
        except ValueError as e:
            print(f'Invalid input: {e}')
        except KeyboardInterrupt:
            print('\nProcess interrupted. Exiting...')
            break