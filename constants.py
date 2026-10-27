import sys

# Application configuration defaults
APP_NAME = "automation-tool-12"
VERSION = "1.0.0"

# Timing constraints in seconds
DEFAULT_CLICK_INTERVAL = 0.1
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0

# Coordinate system boundaries
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Mouse button identifiers
LEFT_BUTTON = "left"
RIGHT_BUTTON = "right"
MIDDLE_BUTTON = "middle"

# Status codes for execution flow
STATUS_IDLE = 0
STATUS_RUNNING = 1
STATUS_ERROR = 2

# Logging configuration
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = "automation.log"

def get_platform():
    """Return the operating system identifier."""
    return sys.platform

# Supported platforms for automation hooks
SUPPORTED_PLATFORMS = ["win32", "linux", "darwin"]