import os

# Configuration constants for automation-tool-12

DEFAULT_CONFIG_DIR = os.path.expanduser('~/.autoclicker')
CONFIG_FILE = os.path.join(DEFAULT_CONFIG_DIR, 'settings.json')

# Timing constraints in milliseconds
MIN_INTERVAL_MS = 10
MAX_INTERVAL_MS = 60000

# Supported mouse buttons mapping
MOUSE_BUTTONS = {
    'left': 'left',
    'right': 'right',
    'middle': 'middle'
}

# Logging levels and formats
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'automation.log'

# Coordinate defaults for screen simulation
DEFAULT_X = 0
DEFAULT_Y = 0

def get_app_defaults():
    """Returns the default dictionary for tool configuration."""
    return {
        'interval': 100,
        'button': MOUSE_BUTTONS['left'],
        'repeat': True,
        'max_clicks': 1000
    }