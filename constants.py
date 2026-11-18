import os

# Application configuration constants for automation-tool-12

DEFAULT_CLICK_INTERVAL = 0.1
MAX_CLICK_LIMIT = 10000

# UI and Display Settings
WINDOW_TITLE = "Automation Tool 12 - Control Panel"
DEFAULT_DPI_AWARE = True

# File System Paths
LOG_DIR = os.path.join(os.getcwd(), "logs")
CONFIG_FILE = "settings.json"

# Execution States
STATE_IDLE = 0
STATE_RUNNING = 1
STATE_PAUSED = 2

# Keyboard Shortcuts
TOGGLE_HOTKEY = "f8"
EXIT_HOTKEY = "f12"

# Validation Constraints
MIN_INTERVAL = 0.01
MAX_INTERVAL = 60.0

def get_app_version():
    return "1.2.0"
