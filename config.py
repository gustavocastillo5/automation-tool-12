import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "double_click": False,
    "max_clicks": 0,
    "toggle_hotkey": "f6",
    "jitter_range": 0.01,
}


class ConfigLoader:
    """Handles loading and saving autoclicker settings with fallback defaults."""

    def __init__(self, config_filename: str = "config.json") -> None:
        self.config_path = Path(config_filename)
        self.current_config: Dict[str, Any] = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load config from JSON file, creating default file if absent."""
        if not self.config_path.exists():
            self.save(DEFAULT_CONFIG)
            return self.current_config.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as file:
                user_data = json.load(file)
                if isinstance(user_data, dict):
                    self.current_config.update(user_data)
        except (json.JSONDecodeError, IOError):
            pass

        return self.current_config.copy()

    def save(self, data: Dict[str, Any] = None) -> None:
        """Save configuration dictionary back to disk."""
        save_data = data if data is not None else self.current_config
        with open(self.config_path, "w", encoding="utf-8") as file:
            json.dump(save_data, file, indent=4)
