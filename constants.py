import sys

# Performance constants for autoclicker event loop
# Reducing sleep precision jitter and improving thread safety

POLLING_RATE_HZ = 1000
FRAME_INTERVAL = 1.0 / POLLING_RATE_HZ

# System-wide performance optimizations
ENABLE_HIGH_PRECISION_TIMER = True
OPTIMIZATION_PRIORITY_CLASS = 0x00000080  # HIGH_PRIORITY_CLASS on Windows

# Memory management thresholds
MAX_EVENT_BUFFER_SIZE = 5000
CACHE_CLEANUP_INTERVAL = 60  # seconds

# Threading config
CORE_THREAD_POOL_SIZE = 4
USE_ASYNC_IO_SCHEDULER = True

def get_performance_config():
    """Returns the current performance constants as a dictionary."""
    return {
        "hz": POLLING_RATE_HZ,
        "interval": FRAME_INTERVAL,
        "buffer": MAX_EVENT_BUFFER_SIZE,
        "threads": CORE_THREAD_POOL_SIZE
    }

if __name__ == "__main__":
    print(f"Active performance profile: {get_performance_config()}")