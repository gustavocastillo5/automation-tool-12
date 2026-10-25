import json
import os
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "hotkey": "f6",
    "repeat_count": 0,  # 0 indicates infinite repetition
    "randomize_interval": False,
    "jitter_range_ms": 15,
}


class ConfigLoader:
    """Manages application configuration loading and default fallbacks."""

    def __init__(self, config_file: str = "config.json") -> None:
        self.config_path = Path(config_file)
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Loads configuration from JSON file, merging with default settings."""
        if not self.config_path.exists():
            self.save(self.config)
            return self.config

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    self.config.update(user_config)
        except (json.JSONDecodeError, OSError) as err:
            # Fall back to default settings on read error or corrupt file
            print(f"Warning: Failed to load config file ({err}). Using defaults.")

        return self.config

    def save(self, settings: Dict[str, Any] = None) -> bool:
        """Saves active configuration to disk."""
        if settings is not None:
            self.config.update(settings)

        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except OSError as err:
            print(f"Error saving configuration file: {err}")
            return False
