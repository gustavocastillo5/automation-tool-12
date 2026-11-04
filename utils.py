import json
from pathlib import Path
from typing import Any, Dict, List, Union


def load_click_profile(file_path: Union[str, Path]) -> Dict[str, Any]:
    """Load click sequence profile configuration from JSON file."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Profile file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if "clicks" not in data or not isinstance(data["clicks"], list):
        raise ValueError("Invalid profile format: 'clicks' list missing")

    return data


def save_click_profile(file_path: Union[str, Path], profile_data: Dict[str, Any]) -> bool:
    """Save click sequence configuration data to a target JSON file."""
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if "clicks" not in profile_data:
        profile_data["clicks"] = []

    with path.open("w", encoding="utf-8") as f:
        json.dump(profile_data, f, indent=4)

    return True


def calculate_click_statistics(delays: List[float]) -> Dict[str, float]:
    """Calculate average, min, max delay timings and clicks per second."""
    if not delays:
        return {"avg_delay": 0.0, "min_delay": 0.0, "max_delay": 0.0, "cps": 0.0}

    total = sum(delays)
    avg = total / len(delays)
    min_val = min(delays)
    max_val = max(delays)
    cps = 1.0 / avg if avg > 0 else 0.0

    return {
        "avg_delay": round(avg, 4),
        "min_delay": round(min_val, 4),
        "max_delay": round(max_val, 4),
        "cps": round(cps, 2),
    }
