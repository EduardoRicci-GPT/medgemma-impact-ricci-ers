import os
import json
import logging

class FileIOUtils:
    @staticmethod
    def read_json(file_path):
        """Reads a JSON file and returns its contents as a dictionary."""
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            return None
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        """Writes a dictionary to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"Data written to {file_path}")

    @staticmethod
    def read_text(file_path):
        """Reads a text file and returns its contents."""
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            return None
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_text(file_path, content):
        """Writes content to a text file."""
        with open(file_path, 'w') as file:
            file.write(content)
            logging.info(f"Content written to {file_path}")

