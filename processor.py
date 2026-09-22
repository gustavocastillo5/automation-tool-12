import json
import os
from typing import Dict, Any, Optional

class ClickDataProcessor:
    """Handles persistence and validation for autoclicker settings."""

    def __init__(self, storage_path: str = "config.json"):
        self.storage_path = storage_path

    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Serializes click configuration to disk."""
        try:
            with open(self.storage_path, "w") as f:
                json.dump(settings, f, indent=4)
            return True
        except (IOError, TypeError):
            return False

    def load_settings(self) -> Optional[Dict[str, Any]]:
        """Reads and parses click settings from file."""
        if not os.path.exists(self.storage_path):
            return None
            
        try:
            with open(self.storage_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return None

    def validate_coords(self, data: Dict[str, Any]) -> bool:
        """Ensures click coordinates are within logical bounds."""
        x = data.get("x", 0)
        y = data.get("y", 0)
        return isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0