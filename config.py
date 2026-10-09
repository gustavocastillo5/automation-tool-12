import json
from pathlib import Path
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "button": "left",
    "click_type": "single",
    "max_clicks": 0,
    "hotkey_toggle": "f6",
    "random_delay_range": 0.02,
}

class ConfigLoader:
    """Handles loading, merging, and persisting autoclicker settings."""

    def __init__(self, filepath: str = "config.json"):
        self.filepath = Path(filepath)
        self.config = DEFAULT_CONFIG.copy()

    def load(self) -> Dict[str, Any]:
        """Load configuration from JSON file, falling back to defaults for missing keys."""
        if not self.filepath.exists():
            self.save(self.config)
            return self.config

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                user_config = json.load(f)
                if isinstance(user_config, dict):
                    for key, value in user_config.items():
                        if key in self.config:
                            self.config[key] = value
        except (json.JSONDecodeError, OSError):
            # Return default config if file is corrupted or unreadable
            return DEFAULT_CONFIG.copy()

        return self.config

    def save(self, data: Dict[str, Any] = None) -> bool:
        """Save configuration dictionary to disk."""
        target_data = data if data is not None else self.config
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(target_data, f, indent=4)
            return True
        except OSError:
            return False
