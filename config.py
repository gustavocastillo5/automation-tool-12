import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # Delay between clicks in seconds
    "mouse_button": "left",  # 'left', 'right', or 'middle'
    "click_type": "single",  # 'single' or 'double'
    "hotkey": "f6",  # Toggle start/stop hotkey
    "max_clicks": 0,  # 0 for unlimited clicks
    "randomize_interval": False,  # Add jitter to avoid detection
    "jitter_range": 0.02,  # Interval variation range
}


class ConfigLoader:
    """Handles loading, saving, and merging autoclicker configuration settings."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = Path(config_path)
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from disk, writing standard defaults if file is absent."""
        if not self.config_path.exists():
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded_config = json.load(f)

            # Merge loaded values over defaults to handle missing keys
            config = DEFAULT_CONFIG.copy()
            config.update(loaded_config)
            return config
        except (json.JSONDecodeError, OSError):
            # Return standard fallback configuration if file reading fails
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any]) -> None:
        """Persists current configuration options to the JSON file."""
        with open(self.config_path, "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a specific setting value by key."""
        return self.config.get(key, default)
