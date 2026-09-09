import time

def high_precision_sleep(duration: float) -> None:
    """
    Suspends execution with sub-millisecond precision.

    Combines standard OS-level sleep to release CPU cycles with a
    high-frequency spin lock to guarantee microsecond-level accuracy,
    which is essential for stable high-frequency click simulation.
    """
    if duration <= 0:
        return

    start_time = time.perf_counter()
    target_time = start_time + duration

    if duration > 0.010:
        time.sleep(duration - 0.005)

    while time.perf_counter() < target_time:
        pass

def calculate_click_delay(cps: float) -> float:
    """
    Computes the delay between consecutive clicks based on Clicks Per Second.
    """
    if cps <= 0.0:
        return 0.0
    return round(1.0 / cps, 6)
