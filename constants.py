import sys

# Optimized timing constants for high-frequency input
# Using lower values to minimize CPU overhead per click

POLLING_RATE_HZ = 1000
FRAME_INTERVAL = 1.0 / POLLING_RATE_HZ

# Thread safety buffers for asynchronous event processing
MAX_QUEUE_SIZE = 1024
BUFFER_THRESHOLD = 256

# System resource limits for performance stability
MAX_CPU_PERCENT = 80.0
MEMORY_LIMIT_MB = 512

# Performance-oriented input event flags
EVENT_FLAG_HARDWARE = 0x0001
EVENT_FLAG_SYNCHRONOUS = 0x0002

# Interaction delay tuning
MIN_CLICK_LATENCY_MS = 0.5
MAX_CLICK_LATENCY_MS = 2.0

# Memory alignment for low-latency buffers
BUFFER_ALIGNMENT = 64

def get_performance_mode():
    """Determines environment capability for tuning."""
    return "high_performance" if sys.platform != "win32" else "standard"

PERFORMANCE_MODE = get_performance_mode()