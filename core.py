import json
import os

class DataHandler:
    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """Load data from a JSON file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self, data):
        """Save data to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def update_data(self, key, value):
        """Update a key-value pair in the data."""
        self.data[key] = value
        self.save_data(self.data)

    def get_data(self, key):
        """Retrieve a value by key from the data."""
        return self.data.get(key, None)

# Example usage
if __name__ == '__main__':
    handler = DataHandler('clicker_data.json')
    handler.update_data('click_interval', 0.1)
    print(handler.get_data('click_interval'))  # Output: 0.1
