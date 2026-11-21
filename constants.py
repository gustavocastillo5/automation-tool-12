import platform

# Application identity
APP_NAME = "automation-tool-12"
VERSION = "1.0.0"

# Timing constraints
DEFAULT_INTERVAL = 0.1
MIN_INTERVAL = 0.01
MAX_INTERVAL = 10.0

# OS-specific mouse button mappings
MOUSE_BUTTONS = {
    "left": 1,
    "right": 2,
    "middle": 3
}

# Platform identification for cross-platform driver compatibility
SYSTEM_PLATFORM = platform.system()

# Configuration file paths
CONFIG_FILE_NAME = "config.json"
LOG_FILE_NAME = "automation.log"

# Error codes and exit states
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

def get_app_header() -> str:
    """Returns the formatted application header string."""
    return f"{APP_NAME} v{VERSION} [{SYSTEM_PLATFORM}]"