import sys

# Optimization parameters for mouse event processing
# Reducing polling frequency and buffer sizes to save CPU cycles

DEFAULT_CLICK_INTERVAL = 0.01  # Minimum delay in seconds
MAX_BUFFER_SIZE = 1024         # Cap for event queue to prevent memory bloat
POLL_RATE_HZ = 120           # Target refresh rate for the input loop

# System interaction constants
IS_WINDOWS = sys.platform == 'win32'
IS_LINUX = sys.platform.startswith('linux')
IS_DARWIN = sys.platform == 'darwin'

# Configuration defaults
BATCH_EXECUTION_SIZE = 50      # Number of events per atomic cycle
THREAD_POOL_WORKERS = 4        # Optimized for standard mouse event throughput

def get_cycle_delay() -> float:
    """Calculates wait time based on poll rate."""
    return 1.0 / POLL_RATE_HZ

# Event priority levels
PRIORITY_HIGH = 2
PRIORITY_NORMAL = 1
PRIORITY_LOW = 0