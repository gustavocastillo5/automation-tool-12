import json
import os

DEFAULT_CONFIG = {
    "click_interval": 0.1,
    "button": "left",
    "hotkey": "f6",
    "repeat_count": 0
}

class ConfigLoader:
    """Handles loading and persistence of tool configuration."""
    def __init__(self, config_path="config.json"):
        self.path = config_path
        self.config = self._load_or_create()

    def _load_or_create(self):
        """Loads config from disk or returns defaults."""
        if not os.path.exists(self.path):
            self._save(DEFAULT_CONFIG)
            return DEFAULT_CONFIG
        
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
                # Ensure all default keys exist if file is outdated
                return {**DEFAULT_CONFIG, **data}
        except (json.JSONDecodeError, IOError):
            return DEFAULT_CONFIG

    def _save(self, data):
        """Persists current configuration to json file."""
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))