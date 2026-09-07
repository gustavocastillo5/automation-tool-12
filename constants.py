import platform

# Application configuration constants
APP_NAME = "automation-tool-12"
VERSION = "1.0.0"

# Timing and execution defaults
DEFAULT_CLICK_INTERVAL = 0.5
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0

# Platform identification for OS-specific hooks
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# UI and layout parameters
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

# Mouse button identifiers
BUTTON_LEFT = "left"
BUTTON_RIGHT = "right"
BUTTON_MIDDLE = "middle"

# Validation ranges
MAX_RETRIES = 3
TIMEOUT_SECONDS = 5.0

# Exit codes
EXIT_SUCCESS = 0
EXIT_ERROR = 1