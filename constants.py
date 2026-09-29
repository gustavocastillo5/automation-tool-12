from typing import Final, Dict, Any

# Configuration constants for the automation-tool-12

DEFAULT_INTERVAL: Final[float] = 0.5
MIN_INTERVAL: Final[float] = 0.01
MAX_INTERVAL: Final[float] = 60.0

BUTTON_LEFT: Final[str] = 'left'
BUTTON_RIGHT: Final[str] = 'right'
BUTTON_MIDDLE: Final[str] = 'middle'

SUPPORTED_BUTTONS: Final[tuple[str, ...]] = (BUTTON_LEFT, BUTTON_RIGHT, BUTTON_MIDDLE)

DEFAULT_CONFIG: Final[Dict[str, Any]] = {
    'interval': DEFAULT_INTERVAL,
    'button': BUTTON_LEFT,
    'clicks_per_burst': 1,
    'randomize_delay': False
}

EXIT_KEYS: Final[list[str]] = ['esc', 'f10']

def get_version() -> str:
    """Return the current version of the automation tool."""
    return "1.0.2"

# Logging configuration constants
LOG_FORMAT: Final[str] = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_LEVEL: Final[str] = 'INFO'