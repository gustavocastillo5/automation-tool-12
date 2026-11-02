import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('automation-tool-12')

def validate_click_params(interval, iterations):
    """Ensures click parameters are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError(f"Invalid interval: {interval}. Must be >= 0.01s")
    if not isinstance(iterations, int) or iterations < 0:
        raise ValueError(f"Invalid iterations: {iterations}. Must be positive integer")
    return True

def run_click_loop(interval, iterations):
    """Main execution loop for autoclicker with input validation."""
    try:
        validate_click_params(interval, iterations)
        logger.info(f"Starting automation: {iterations} clicks at {interval}s interval")
        
        for i in range(iterations):
            # Simulating click logic
            time.sleep(interval)
            logger.info(f"Click action performed: {i+1}/{iterations}")
            
        logger.info("Automation sequence completed successfully")
    except ValueError as e:
        logger.error(f"Validation failure: {e}")
    except KeyboardInterrupt:
        logger.warning("Automation stopped by user")

if __name__ == '__main__':
    # Example usage for testing
    run_click_loop(0.5, 5)