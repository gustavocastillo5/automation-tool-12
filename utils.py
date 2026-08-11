import os
import json

def load_json(file_path):
    """Load JSON data from a file."""
    if not os.path.isfile(file_path):
        raise ValueError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def get_file_extension(file_name):
    """Return the file extension for a given file name."""
    return os.path.splitext(file_name)[1]


def ensure_directory_exists(directory):
    """Create directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)


def read_file_lines(file_path):
    """Read lines from a file and return as a list."""
    with open(file_path, 'r') as file:
        return file.readlines()  


def write_lines_to_file(file_path, lines):
    """Write a list of lines to a file."""
    with open(file_path, 'w') as file:
        file.writelines(lines)
