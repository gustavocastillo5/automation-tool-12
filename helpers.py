import json
import random
from typing import List, Dict, Any


def parse_click_sequence(raw_data: str) -> List[Dict[str, Any]]:
    """Parse and validate click profile JSON data into structured events."""
    try:
        events = json.loads(raw_data)
        if not isinstance(events, list):
            raise ValueError("Profile data must be a JSON array of events")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format in profile data: {e}")

    validated_events = []
    for idx, event in enumerate(events):
        if not isinstance(event, dict):
            continue

        x = event.get("x", 0)
        y = event.get("y", 0)
        delay = max(0.0, float(event.get("delay", 0.1)))
        button = str(event.get("button", "left")).lower()

        validated_events.append({
            "id": idx + 1,
            "x": int(x),
            "y": int(y),
            "delay": delay,
            "button": button if button in ("left", "right", "middle") else "left",
        })

    return validated_events


def calculate_jittered_delay(base_delay: float, jitter_ratio: float = 0.1) -> float:
    """Calculate randomized delay variation to simulate human timing."""
    if base_delay <= 0:
        return 0.0
    variation = base_delay * min(max(jitter_ratio, 0.0), 1.0)
    return max(0.001, base_delay + random.uniform(-variation, variation))


def format_sequence_summary(events: List[Dict[str, Any]]) -> str:
    """Generate readable summary statistics for click profile sequence."""
    total_clicks = len(events)
    total_duration = sum(e.get("delay", 0.0) for e in events)
    return f"Sequence: {total_clicks} clicks | ~{total_duration:.2f}s duration"
