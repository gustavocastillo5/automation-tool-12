import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_clicks(interval, iterations):
    """Executes automation loop with input validation."""
    # Validate input constraints
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a number at least 0.01 seconds.")
    
    if not isinstance(iterations, int) or iterations < 1:
        raise ValueError("Iterations must be a positive integer.")

    logger.info(f"Starting automation: {iterations} clicks at {interval}s interval")
    
    try:
        for i in range(iterations):
            # Simulating click logic
            logger.info(f"Execution step {i + 1}/{iterations}")
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.warning("Automation interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error during execution: {e}")

if __name__ == "__main__":
    # Example usage with safe inputs
    try:
        process_clicks(interval=0.5, iterations=5)
    except ValueError as err:
        logger.error(f"Invalid configuration: {err}")