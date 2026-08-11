import json
import os

class ConfigLoader:
    def __init__(self, default_config_path):
        self.default_config_path = default_config_path
        self.config = self.load_default_config()

    def load_default_config(self):
        """Load default configuration from a JSON file."""
        if not os.path.exists(self.default_config_path):
            raise FileNotFoundError(f"Configuration file not found: {self.default_config_path}")
        with open(self.default_config_path, 'r') as file:
            return json.load(file)

    def get(self, key, default=None):
        """Retrieve a configuration value by key, returning a default if not found."""
        return self.config.get(key, default)

# Example usage:
if __name__ == '__main__':
    loader = ConfigLoader('default_config.json')
    print(loader.get('some_key', 'default_value'))