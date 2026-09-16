from typing import Dict, Any, Optional
import json
import os

class ConfigManager:
    """Handles loading and saving of autoclicker configuration parameters."""

    def __init__(self, filepath: str = "settings.json") -> None:
        self.filepath: str = filepath
        self.settings: Dict[str, Any] = {
            "interval": 0.1,
            "button": "left",
            "hotkey": "f6",
            "repeat": 0
        }

    def load_config(self) -> None:
        """Reads configuration from a JSON file if it exists."""
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as file:
                self.settings.update(json.load(file))

    def save_config(self) -> None:
        """Persists current settings to the disk."""
        with open(self.filepath, "w") as file:
            json.dump(self.settings, file, indent=4)

    def get_setting(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a specific setting value with an optional fallback."""
        return self.settings.get(key, default)

    def update_setting(self, key: str, value: Any) -> None:
        """Updates a setting key and saves the changes."""
        self.settings[key] = value
        self.save_config()