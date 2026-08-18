import json
from typing import Any, Dict, List

def load_config(file_path: str) -> Dict[str, Any]:
    """Load JSON configuration from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def save_config(data: Dict[str, Any], file_path: str) -> None:
    """Save configuration data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def format_click_data(clicks: List[Dict[str, Any]]) -> List[str]:
    """Format click data for better readability.""" 
    formatted_data = []
    for click in clicks:
        formatted_data.append(f"Position: ({click['x']}, {click['y']}), Delay: {click['delay']}s")
    return formatted_data


def validate_click_data(data: Dict[str, Any]) -> bool:
    """Validate the click data structure."""
    required_keys = {'x', 'y', 'delay'}
    return all(key in data for key in required_keys) 


def parse_clicks(raw_data: str) -> List[Dict[str, Any]]:
    """Parse raw click data into structured format."""
    clicks = []
    lines = raw_data.strip().split('\n')
    for line in lines:
        x, y, delay = map(float, line.split(','))
        clicks.append({'x': x, 'y': y, 'delay': delay})
    return clicks
