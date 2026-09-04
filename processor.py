import time
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def validate_inputs(clicks, interval):
    """Ensures click count and interval are within safe parameters."""
    if not isinstance(clicks, int) or clicks <= 0:
        raise ValueError("Click count must be a positive integer.")
    if not isinstance(interval, (int, float)) or interval < 0.1:
        raise ValueError("Interval must be at least 0.1 seconds.")
    return True

def run_clicker(clicks: int, interval: float):
    """Main processing loop with input validation."""
    try:
        validate_inputs(clicks, interval)
        logger.info(f"Starting automation for {clicks} clicks.")
        
        for i in range(1, clicks + 1):
            # Simulate mouse click logic here
            logger.debug(f"Executing click {i}/{clicks}")
            time.sleep(interval)
            
        logger.info("Automation sequence completed successfully.")
    except ValueError as e:
        logger.error(f"Validation failure: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during execution: {e}")

if __name__ == '__main__':
    # Example usage for testing loop stability
    run_clicker(5, 0.5)