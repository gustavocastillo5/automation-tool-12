import os
import json
import logging

# Configuration settings for automation-tool-12
DEFAULT_CONFIG = {
    "interval": 0.1,
    "iterations": 100,
    "button": "left"
}

def load_config(path: str) -> dict:
    """Loads and validates configuration from a JSON file."""
    if not os.path.exists(path):
        logging.warning(f"Config file missing at {path}, using defaults.")
        return DEFAULT_CONFIG

    try:
        with open(path, "r") as file:
            data = json.load(file)
            # Ensure mandatory keys exist with valid types
            if not isinstance(data.get("interval"), (int, float)):
                raise ValueError("Invalid interval type")
            return data
    except (json.JSONDecodeError, ValueError, PermissionError) as e:
        logging.error(f"Failed to load config: {e}. Falling back to defaults.")
        return DEFAULT_CONFIG

def save_config(path: str, config: dict) -> bool:
    """Persists configuration safely to disk."""
    try:
        with open(path, "w") as file:
            json.dump(config, file, indent=4)
        return True
    except (IOError, TypeError) as e:
        logging.error(f"Could not save configuration: {e}")
        return False