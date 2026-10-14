import sys
import time

# Performance optimization constants for autoclicker kernel
# Using small integer caches and interval thresholds

MIN_CLICK_INTERVAL_MS = 10
MAX_CLICK_INTERVAL_MS = 60000

# System-level jitter thresholds to reduce overhead
JITTER_THRESHOLD_FACTOR = 0.05

# Cached time constants for loop efficiency
POLLING_TICK_RATE = 0.001
CPU_IDLE_SLEEP = 0.005

# Platform-specific buffer limits for mouse events
EVENT_BUFFER_SIZE = 128

# Optimized timing calculation using perf_counter
TIMER_FUNCTION = time.perf_counter

def get_performance_thresholds():
    """Return dict of performance tuning constants."""
    return {
        "min_ms": MIN_CLICK_INTERVAL_MS,
        "tick_rate": POLLING_TICK_RATE,
        "buffer_size": EVENT_BUFFER_SIZE
    }
