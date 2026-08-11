import json
import os

DEFAULT_CONFIG = {
    'setting_1': 'default_value_1',
    'setting_2': 'default_value_2',
    'setting_3': 10,
}

class ConfigLoader:
    def __init__(self, config_file=None):
        self.config = DEFAULT_CONFIG.copy()
        if config_file and os.path.exists(config_file):
            self.load_config(config_file)

    def load_config(self, config_file):
        with open(config_file, 'r') as file:
            user_config = json.load(file)
            self.config.update(user_config)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value

    def save(self, config_file):
        with open(config_file, 'w') as file:
            json.dump(self.config, file, indent=4)
