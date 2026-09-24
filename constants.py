from typing import Final

# Configuration constants for the autoclicker engine

DEFAULT_INTERVAL: Final[float] = 0.1
MAX_CLICK_RATE: Final[float] = 1000.0
MIN_CLICK_RATE: Final[float] = 0.01

# Input simulation constants
MOUSE_BUTTON_LEFT: Final[str] = "left"
MOUSE_BUTTON_RIGHT: Final[str] = "right"

# UI and logging defaults
WINDOW_TITLE: Final[str] = "automation-tool-12"
LOG_FILE_PATH: Final[str] = "logs/autoclicker.log"

def get_default_settings() -> dict[str, float]:
    """Returns a dictionary of default application settings."""
    return {
        "interval": DEFAULT_INTERVAL,
        "max_rate": MAX_CLICK_RATE,
        "min_rate": MIN_CLICK_RATE
    }

# Coordinate system constants
SCREEN_ORIGIN_X: Final[int] = 0
SCREEN_ORIGIN_Y: Final[int] = 0

# Exit codes
EXIT_SUCCESS: Final[int] = 0
EXIT_FAILURE: Final[int] = 1