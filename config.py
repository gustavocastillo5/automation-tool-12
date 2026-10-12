import json
import logging
from pathlib import Path
from typing import Any, Dict

logger = logging.getLogger(__name__)

DEFAULT_CONFIG: Dict[str, Any] = {
    "click_interval": 0.1,
    "mouse_button": "left",
    "hotkey": "f6",
    "click_count": 0,
    "random_jitter": 0.01,
    "start_delay": 3.0,
}


class ConfigManager:
    """Handles loading, validating, and saving autoclicker settings."""

    def __init__(self, config_path: str = "config.json") -> None:
        self.config_path = Path(config_path)
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads configuration from file or returns default settings."""
        if not self.config_path.exists():
            logger.info("Config file missing, generating defaults")
            self.save_config(DEFAULT_CONFIG)
            return DEFAULT_CONFIG.copy()

        try:
            with open(self.config_path, "r", encoding="utf-8") as f:
                loaded_config = json.load(f)
            # Merge defaults for any missing keys
            config = DEFAULT_CONFIG.copy()
            config.update(loaded_config)
            return config
        except (json.JSONDecodeError, OSError) as err:
            logger.warning("Failed to load config file (%s), using defaults", err)
            return DEFAULT_CONFIG.copy()

    def save_config(self, config_data: Dict[str, Any] = None) -> None:
        """Saves current or provided configuration to disk."""
        data_to_save = config_data if config_data is not None else self.config
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f, indent=4)
        except OSError as err:
            logger.error("Could not write config file: %s", err)

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a config value by key."""
        return self.config.get(key, default)
