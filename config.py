import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "click_type": "single",
    "repeat_mode": "infinite",
    "repeat_count": 100,
    "hotkey": "f6",
    "target_location": None
}


class ConfigManager:
    """Handles loading, saving, and accessing autoclicker settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.settings: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads settings from JSON file, merging with defaults."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as file:
                    saved_config = json.load(file)
                    if isinstance(saved_config, dict):
                        self.settings.update(saved_config)
            except (json.JSONDecodeError, IOError):
                self.settings = DEFAULT_CONFIG.copy()
        else:
            self.save()
        return self.settings

    def save(self) -> None:
        """Saves current settings to configuration file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as file:
                json.dump(self.settings, file, indent=4)
        except IOError:
            pass

    def get(self, key: str, fallback: Any = None) -> Any:
        """Retrieves a setting key with an optional fallback."""
        return self.settings.get(key, fallback)

    def set(self, key: str, value: Any) -> None:
        """Updates a specific config setting and persists it."""
        self.settings[key] = value
        self.save()
