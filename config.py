import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "clicks_per_second": 10.0,
    "mouse_button": "left",
    "click_type": "single",
    "toggle_hotkey": "f6",
    "jitter_range": 0.02,
    "max_clicks": 0,
}


class ConfigManager:
    """Manages autoclicker settings with fallback defaults."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = filepath
        self._data = DEFAULT_CONFIG.copy()

    def load_config(self) -> Dict[str, Any]:
        """Loads JSON config file and merges missing keys with default settings."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as file:
                    loaded_data = json.load(file)
                    if isinstance(loaded_data, dict):
                        self._data.update(loaded_data)
            except (json.JSONDecodeError, OSError):
                pass
        else:
            self.save_config()

        return self._data

    def save_config(self) -> None:
        """Persists the current configuration dictionary to disk."""
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(self._data, file, indent=4)

    def get(self, key: str) -> Any:
        """Retrieve a configuration option value."""
        return self._data.get(key, DEFAULT_CONFIG.get(key))
