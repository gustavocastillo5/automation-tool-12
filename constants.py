import platform

# platform detection
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
IS_LINUX = platform.system() == "Linux"

# default click settings
DEFAULT_CLICK_INTERVAL = 0.1
DEFAULT_BUTTON = "left"

# input mapping
MOUSE_BUTTON_MAP = {
    "left": 1,
    "middle": 2,
    "right": 3
}

# coordinate boundaries
SCREEN_WIDTH_MIN = 0
SCREEN_HEIGHT_MIN = 0

# timing constants (seconds)
MIN_DELAY = 0.001
MAX_DELAY = 60.0

# retry configuration
MAX_RETRIES = 3
RETRY_DELAY = 0.5

# logging format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = "INFO"