import time
import logging
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """Executes a network-dependent function with exponential backoff."""
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Critical failure: {e}")
            raise
            
    logger.error("Maximum retries reached. Operation failed.")
    raise last_exception or Exception("Unknown network error")

class NetworkProcessor:
    """Handles automated network clicks with integrated retry mechanism."""
    def __init__(self, target_url: str):
        self.target_url = target_url

    def perform_click(self, action_payload: dict) -> bool:
        def request_task():
            # Simulate network activity for autoclicker
            print(f"Executing click on {self.target_url}")
            return True
            
        try:
            return execute_with_retry(request_task)
        except Exception:
            return False