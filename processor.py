import json
import os
from typing import Dict, Any, Optional

class ClickDataHandler:
    def __init__(self, storage_path: str = "data.json"):
        self.storage_path = storage_path

    def load_configuration(self) -> Dict[str, Any]:
        if not os.path.exists(self.storage_path):
            return {"interval": 0.1, "button": "left", "repeats": 0}
        
        try:
            with open(self.storage_path, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_configuration(self, data: Dict[str, Any]) -> bool:
        try:
            with open(self.storage_path, "w") as f:
                json.dump(data, f, indent=4)
            return True
        except IOError:
            return False

    def validate_settings(self, settings: Dict[str, Any]) -> bool:
        required = {"interval", "button", "repeats"}
        return all(key in settings for key in required) and settings["interval"] > 0

def get_default_settings() -> Dict[str, Any]:
    return {"interval": 0.5, "button": "left", "repeats": 10}