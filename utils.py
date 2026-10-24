import random
from typing import List, Dict, Tuple, Any


def cps_to_interval(cps: float) -> float:
    """Convert clicks per second (CPS) to time interval in seconds."""
    if cps <= 0:
        raise ValueError("CPS must be greater than zero.")
    return 1.0 / cps


def interval_to_cps(interval: float) -> float:
    """Convert time interval in seconds to clicks per second (CPS)."""
    if interval <= 0:
        raise ValueError("Interval must be greater than zero.")
    return 1.0 / interval


def apply_jitter(base_interval: float, variance_ms: float) -> float:
    """Apply a random millisecond variance to a base interval for human-like timing."""
    if base_interval <= 0:
        return 0.001
    variance_sec = variance_ms / 1000.0
    jittered = base_interval + random.uniform(-variance_sec, variance_sec)
    return max(0.001, jittered)


def parse_click_profile(raw_data: List[Dict[str, Any]]) -> List[Tuple[int, int, float]]:
    """
    Parse raw coordinate and delay dictionary records into validated click sequences.
    Returns a list of tuples formatted as (x, y, delay_seconds).
    """
    parsed_sequence = []
    for entry in raw_data:
        x = max(0, int(entry.get("x", 0)))
        y = max(0, int(entry.get("y", 0)))
        delay = max(0.001, float(entry.get("delay", 0.1)))
        parsed_sequence.append((x, y, delay))
    return parsed_sequence
