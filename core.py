import json
from typing import Any, Dict, List

class AutoClickerData:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict[str, Any]]:
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def save_data(self) -> None:
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.data, file, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_click_event(self, event: Dict[str, Any]) -> None:
        self.data.append(event)
        self.save_data()

    def get_click_events(self) -> List[Dict[str, Any]]:
        return self.data
