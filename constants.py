# Constants used throughout the autoclicker tool

# Default configuration settings
DEFAULT_CLICK_INTERVAL = 0.1  # in seconds
DEFAULT_BUTTON = 'left'
DEFAULT_REPEAT_COUNT = 100

# Predefined mouse actions
MOUSE_ACTIONS = {
    'left_click': 'left',
    'right_click': 'right',
    'double_click': 'double',
}

# Application settings
WINDOW_TITLE = 'Autoclicker'
MAXIMUM_CLICKS_PER_SECOND = 20

# File paths
CONFIG_FILE_PATH = 'config.json'
LOG_FILE_PATH = 'autoclicker.log'

# Message constants
ERROR_MESSAGES = {
    'file_not_found': 'The specified file could not be found.',
    'invalid_configuration': 'Configuration is invalid or missing required keys.',
}

# Success messages
SUCCESS_MESSAGES = {
    'operation_complete': 'The operation completed successfully.',
    'clicks_executed': 'Clicks have been executed.',
}