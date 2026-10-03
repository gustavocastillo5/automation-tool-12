import json
from typing import Dict, Any, Optional

class ConfigManager:
    """Handles loading and saving of autoclicker settings."""

    def __init__(self, filepath: str = "settings.json") -> None:
        self.filepath: str = filepath
        self.settings: Dict[str, Any] = {
            "interval": 0.1,
            "button": "left",
            "repeat": True
        }

    def load(self) -> Dict[str, Any]:
        """Reads configuration from a JSON file."""
        try:
            with open(self.filepath, "r") as file:
                self.settings.update(json.load(file))
        except (FileNotFoundError, json.JSONDecodeError):
            self.save()
        return self.settings

    def save(self) -> None:
        """Writes current settings to a JSON file."""
        with open(self.filepath, "w") as file:
            json.dump(self.settings, file, indent=4)

    def update(self, key: str, value: Any) -> None:
        """Updates a specific setting key-value pair."""
        self.settings[key] = value
        self.save()

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """Retrieves a setting with an optional default fallback."""
        return self.settings.get(key, default)