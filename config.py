import json
import os

DEFAULT_CONFIG = {
    'click_speed': 100,
    'button': 1,
    'duration': 60,
    'repeat': False
}

class ConfigLoader:
    def __init__(self, config_file='config.json'):
        self.config_file = config_file
        self.config = DEFAULT_CONFIG.copy()
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                try:
                    user_config = json.load(file)
                    self.config.update(user_config)
                except json.JSONDecodeError as e:
                    print(f'Error loading config: {e}')

    def get(self, key):
        return self.config.get(key, DEFAULT_CONFIG.get(key))

    def set(self, key, value):
        self.config[key] = value

    def save(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
