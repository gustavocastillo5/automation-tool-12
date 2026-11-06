import json
import os
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,  # Seconds between clicks
    "mouse_button": "left",  # Options: left, right, middle
    "hotkey": "f8",  # Toggle start/stop hotkey
    "max_clicks": 0,  # 0 indicates continuous clicking
    "randomize_interval": False,  # Add jitter to click timing
    "jitter_range": 0.02,  # Max offset in seconds for jitter
}


class ConfigLoader:
    """Loads and manages user configurations with fallback defaults."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from disk, applying defaults for missing keys."""
        config = DEFAULT_CONFIG.copy()

        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    user_config = json.load(f)
                    if isinstance(user_config, dict):
                        config.update(user_config)
            except (json.JSONDecodeError, OSError):
                pass

        return config

    def save_config(self) -> bool:
        """Saves current configuration to file."""
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(self.config, f, indent=4)
            return True
        except OSError:
            return False

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieve a specific configuration value."""
        return self.config.get(key, default)
