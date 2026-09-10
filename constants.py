import sys

# Configuration constraints for the autoclicker
# Used to prevent invalid user inputs and system crashes

MIN_INTERVAL = 0.01  # Minimum delay in seconds
MAX_INTERVAL = 60.0  # Maximum delay in seconds
MAX_RETRIES = 3      # Connection retry attempts

# System specific error codes
ERR_OS_UNSUPPORTED = 1
ERR_PERMISSION_DENIED = 2
ERR_INVALID_CONFIG = 3

def validate_interval(value: float) -> bool:
    """Ensures interval is within safe operating bounds."""
    try:
        return MIN_INTERVAL <= float(value) <= MAX_INTERVAL
    except (ValueError, TypeError):
        return False

def exit_with_error(message: str, code: int) -> None:
    """Standardized exit path for fatal tool errors."""
    print(f"[ERROR] {message}", file=sys.stderr)
    sys.exit(code)

# Application path constants
DEFAULT_CONFIG_PATH = "config.json"
LOG_FILE_PATH = "automation.log"