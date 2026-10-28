import time
import logging

logger = logging.getLogger(__name__)

def process_clicks(interval, iterations):
    """Executes click loop with input validation."""
    # Validate interval range
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a float >= 0.01 seconds")
        
    # Validate iterations range
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("Iterations must be an integer >= 1")

    logger.info(f"Starting automation: {iterations} clicks every {interval}s")
    
    try:
        for i in range(iterations):
            # Simulating click logic
            logger.debug(f"Click {i + 1}/{iterations} performed")
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.warning("Automation sequence interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error during execution: {e}")

def main():
    # Example usage parameters
    params = {'interval': 0.5, 'iterations': 10}
    
    try:
        process_clicks(params['interval'], params['iterations'])
    except ValueError as e:
        logger.error(f"Configuration error: {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()