import sys
from enum import Enum, unique


@unique
class ClickButton(str, Enum):
    """Mouse buttons supported by the autoclicker."""

    LEFT = "left"
    RIGHT = "right"
    MIDDLE = "middle"


@unique
class ClickType(str, Enum):
    """Click actions supported by the engine."""

    SINGLE = "single"
    DOUBLE = "double"
    HOLD = "hold"


# Timing and execution defaults
DEFAULT_DELAY_SECONDS = 0.1
DEFAULT_INTERVAL_SECONDS = 1.0
DEFAULT_CLICK_COUNT = 0  # Zero represents infinite loops

# Default keyboard control hotkeys
DEFAULT_START_HOTKEY = "f6"
DEFAULT_STOP_HOTKEY = "f7"
DEFAULT_EXIT_HOTKEY = "f8"

# Safe operational boundaries to prevent thread locking
MIN_DELAY_LIMIT = 0.001
MAX_DELAY_LIMIT = 86400.0  # 24 hours

# Operating system flags
IS_WINDOWS = sys.platform == "win32"
IS_MACOS = sys.platform == "darwin"
IS_LINUX = sys.platform.startswith("linux")
