import dataclasses
from typing import Dict, Any

@dataclasses.dataclass
class ClickConfig:
    """Configuration settings for the autoclicker."""
    interval_ms: int = 100
    button: str = "left"
    repeat_count: int = 1
    randomize_timing: bool = False

def load_config(data: Dict[str, Any]) -> ClickConfig:
    """
    Create a ClickConfig instance from a dictionary.

    Args:
        data: A dictionary containing configuration keys.

    Returns:
        An initialized ClickConfig object with sanitized values.
    """
    return ClickConfig(
        interval_ms=int(data.get("interval_ms", 100)),
        button=str(data.get("button", "left")),
        repeat_count=int(data.get("repeat_count", 1)),
        randomize_timing=bool(data.get("randomize_timing", False))
    )

def get_default_config() -> ClickConfig:
    """
    Returns a default configuration set.

    Returns:
        Default ClickConfig object.
    """
    return ClickConfig()