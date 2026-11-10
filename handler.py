import time
import logging
from typing import Callable, Any

logger = logging.getLogger(__name__)

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Execute a function with simple exponential backoff."""
    last_exception = None
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            last_exception = e
            logger.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(delay * (2 ** attempt))
    
    logger.error(f"Operation failed after {retries} attempts")
    raise last_exception

def network_safe_call(action: Callable) -> Any:
    """
    Wrapper for network-dependent automation tasks.
    Ensures persistence against transient connection drops.
    """
    try:
        return execute_with_retry(action, retries=3, delay=2.0)
    except Exception:
        # Final fallback for the autoclicker state machine
        logger.critical("Network recovery exhausted, resetting automation flow")
        return None