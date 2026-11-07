import time
import logging
import urllib.request
import urllib.error
from typing import Callable, Any, Optional

logger = logging.getLogger(__name__)

class NetworkHandler:
    """Handles network requests with built-in retry logic for autoclicker configs."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 1.5, timeout: float = 5.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.timeout = timeout

    def execute_with_retry(self, operation: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        """Executes a network callable with exponential backoff retries."""
        attempt = 0
        delay = 1.0

        while attempt < self.max_retries:
            try:
                return operation(*args, **kwargs)
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                attempt += 1
                if attempt >= self.max_retries:
                    logger.error(f"Network operation failed after {attempt} attempts: {exc}")
                    raise exc
                
                logger.warning(
                    f"Attempt {attempt}/{self.max_retries} failed ({exc}). Retrying in {delay:.1f}s..."
                )
                time.sleep(delay)
                delay *= self.backoff_factor

    def fetch_remote_preset(self, url: str) -> Optional[bytes]:
        """Fetch click sequence preset from remote endpoint with retry mechanism."""
        def _request():
            req = urllib.request.Request(url, headers={'User-Agent': 'Autoclicker-Client/1.2'})
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read()

        try:
            return self.execute_with_retry(_request)
        except Exception as e:
            logger.critical(f"Failed to fetch remote preset from {url}: {e}")
            return None

    def send_telemetry(self, endpoint: str, data: bytes) -> bool:
        """Post session click metrics to telemetry server with retry logic."""
        def _post():
            req = urllib.request.Request(
                endpoint,
                data=data,
                headers={'Content-Type': 'application/json'},
                method='POST'
            )
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.status == 200

        try:
            return bool(self.execute_with_retry(_post))
        except Exception:
            return False
