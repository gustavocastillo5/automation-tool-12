from typing import Final, Dict, Any

# Application configuration constants for automation-tool-12

DEFAULT_CLICK_INTERVAL: Final[float] = 0.1
MAX_CLICK_LIMIT: Final[int] = 10000
DEFAULT_MOUSE_BUTTON: Final[str] = "left"

# Coordinate mapping for UI elements
UI_LAYOUT_MAP: Final[Dict[str, tuple[int, int]]] = {
    "start_button": (100, 200),
    "stop_button": (150, 200),
    "settings_panel": (500, 500)
}

# Error codes for the automation engine
ERR_CODES: Final[Dict[str, int]] = {
    "DRIVER_NOT_FOUND": 101,
    "PERMISSION_DENIED": 102,
    "INTERRUPTED_BY_USER": 103
}

def get_app_metadata() -> Dict[str, Any]:
    """Returns the dictionary containing tool metadata."""
    return {
        "version": "1.2.0",
        "name": "automation-tool-12",
        "author": "Developer"
    }