import json
import logging
from pathlib import Path
from typing import Dict, Any

# Configure logging for automation-tool-12
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('autoclicker')

def save_click_data(filepath: str, data: Dict[str, Any]) -> None:
    """Persists autoclicker configuration to a local JSON file."""
    try:
        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Successfully saved configuration to {filepath}")
    except (IOError, TypeError) as e:
        logger.error(f"Failed to save data: {e}")

def load_click_data(filepath: str) -> Dict[str, Any]:
    """Retrieves stored click settings from a JSON file."""
    path = Path(filepath)
    if not path.exists():
        logger.warning(f"Configuration file {filepath} not found")
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Data corruption in {filepath}: {e}")
        return {}