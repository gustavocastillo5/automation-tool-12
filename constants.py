import platform
from enum import Enum

# Application configuration defaults
DEFAULT_INTERVAL = 0.1
DEFAULT_CLICK_TYPE = 'left'
DEFAULT_HOTKEY = 'f8'

# Supported mouse buttons
class MouseButton(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    MIDDLE = 'middle'

# Platform-specific thresholds for automation safety
OS_TYPE = platform.system()
IS_WINDOWS = OS_TYPE == 'Windows'

# UI and Interaction constraints
MAX_CLICK_RATE = 1000
MIN_INTERVAL = 0.001
TIMEOUT_SECONDS = 30

# Log formatting
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE_PATH = 'automation.log'

def get_app_title() -> str:
    return "Automation Tool 12 - Autoclicker"