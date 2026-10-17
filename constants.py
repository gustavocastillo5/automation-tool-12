from typing import Final

# Screen coordinate bounds for click events
MAX_SCREEN_WIDTH: Final[int] = 3840
MAX_SCREEN_HEIGHT: Final[int] = 2160

# Timing constraints for automation sequences
MIN_INTERVAL_SECONDS: Final[float] = 0.01
MAX_INTERVAL_SECONDS: Final[float] = 60.0
DEFAULT_CLICK_DURATION: Final[float] = 0.05

# Mouse event identifiers
LEFT_BUTTON: Final[str] = 'left'
RIGHT_BUTTON: Final[str] = 'right'
MIDDLE_BUTTON: Final[str] = 'middle'

# Application configuration defaults
DEFAULT_LOG_FILE: Final[str] = 'automation.log'
DEFAULT_CONFIG_PATH: Final[str] = 'config/settings.yaml'

# System signal mapping
EXIT_SIGNAL: Final[str] = 'ctrl+c'
PAUSE_SIGNAL: Final[str] = 'f10'
RESUME_SIGNAL: Final[str] = 'f11'

def get_app_metadata() -> dict[str, str]:
    """Return constant application metadata.

    Returns:
        dict[str, str]: Versioning and identification mapping.
    """
    return {
        "name": "automation-tool-12",
        "version": "1.0.4",
        "author": "Developer"
    }