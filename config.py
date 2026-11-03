import json
from pathlib import Path
from typing import Any, Dict


class AutoClickerConfig:
    """Manages configuration settings for the autoclicker application."""

    def __init__(
        self,
        interval: float = 0.1,
        button: str = "left",
        click_count: int = 0,
        jitter_range: float = 0.01,
        toggle_key: str = "f6",
    ) -> None:
        """Initialize configuration with default or custom parameters."""
        self.interval: float = interval
        self.button: str = button
        self.click_count: int = click_count
        self.jitter_range: float = jitter_range
        self.toggle_key: str = toggle_key

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration properties to a dictionary format."""
        return {
            "interval": self.interval,
            "button": self.button,
            "click_count": self.click_count,
            "jitter_range": self.jitter_range,
            "toggle_key": self.toggle_key,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AutoClickerConfig":
        """Create an AutoClickerConfig instance from a dictionary."""
        return cls(
            interval=float(data.get("interval", 0.1)),
            button=str(data.get("button", "left")),
            click_count=int(data.get("click_count", 0)),
            jitter_range=float(data.get("jitter_range", 0.01)),
            toggle_key=str(data.get("toggle_key", "f6")),
        )

    def save_to_file(self, file_path: Path) -> None:
        """Save the current configuration to a JSON file."""
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, file_path: Path) -> "AutoClickerConfig":
        """Load configuration from a JSON file if it exists."""
        if not file_path.exists():
            return cls()
        with open(file_path, "r", encoding="utf-8") as file:
            data: Dict[str, Any] = json.load(file)
            return cls.from_dict(data)
