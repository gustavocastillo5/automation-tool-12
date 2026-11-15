import logging
import time
import urllib.error
import urllib.request
from typing import Any, Callable, Optional

logger = logging.getLogger("autoclicker.processor")


class NetworkProcessor:
    """Handles network operations with built-in retry logic for autoclicker services."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 1.5, timeout: float = 5.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

    def execute_with_retry(self, func: Callable[..., Any], *args: Any, **kwargs: Any) -> Optional[Any]:
        """Executes a network callable with exponential backoff retries."""
        delay = 1.0
        for attempt in range(1, self.max_retries + 1):
            try:
                logger.debug(f"Executing request (attempt {attempt}/{self.max_retries})")
                return func(*args, **kwargs)
            except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as exc:
                logger.warning(f"Network operation failed on attempt {attempt}: {exc}")
                if attempt == self.max_retries:
                    logger.error(f"Failed after {self.max_retries} attempts.")
                    raise
                time.sleep(delay)
                delay *= self.backoff_factor

        return None

    def fetch_remote_profile(self, profile_url: str) -> str:
        """Fetch remote click pattern profile with retry handling."""
        def _fetch():
            req = urllib.request.Request(
                profile_url, 
                headers={"User-Agent": "AutomationTool-Autoclicker/1.2"}
            )
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read().decode("utf-8")

        return self.execute_with_retry(_fetch)
