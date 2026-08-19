import json

class AutoClickerDataHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")
            return {}

    def save_data(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def update_data(self, key, value):
        data = self.load_data()
        data[key] = value
        self.save_data(data)

    def delete_key(self, key):
        data = self.load_data()
        if key in data:
            del data[key]
            self.save_data(data)