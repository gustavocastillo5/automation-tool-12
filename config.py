import json
import os

class ConfigError(Exception):
    pass

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config_data = {}
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.filename):
            raise ConfigError(f'Configuration file not found: {self.filename}')
        
        try:
            with open(self.filename, 'r') as file:
                self.config_data = json.load(file)
        except json.JSONDecodeError:
            raise ConfigError('Failed to decode JSON from the configuration file')
        except Exception as e:
            raise ConfigError(f'An unexpected error occurred: {str(e)}')

    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def __getitem__(self, key):
        try:
            return self.config_data[key]
        except KeyError:
            raise ConfigError(f'Key {key} not found in configuration')

    def set(self, key, value):
        self.config_data[key] = value

    def save(self):
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            raise ConfigError(f'Error saving configuration file: {str(e)}')
