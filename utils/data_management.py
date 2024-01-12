import json

def read_data_from_file(file_path: str) -> str:
    """
    Reads data from a file and returns it as a string.

    :param file_path: Path to the file to be read.
    :return: Contents of the file as a string.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"Error reading from file: {e}")
        return None

def write_data_to_file(file_path: str, data: str) -> bool:
    """
    Writes data to a file.

    :param file_path: Path to the file where data will be written.
    :param data: Data to be written to the file.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def load_json_data(file_path: str) -> dict:
    """
    Loads data from a JSON file.

    :param file_path: Path to the JSON file.
    :return: Parsed JSON data as a dictionary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"JSON file not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return {}
    except Exception as e:
        print(f"Error loading JSON data: {e}")
        return {}

def save_json_data(file_path: str, data: dict) -> bool:
    """
    Saves data to a JSON file.

    :param file_path: Path to the JSON file where data will be saved.
    :param data: Data to be saved in JSON format.
    :return: True if the operation is successful, False otherwise.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving JSON data: {e}")
        return False

# Additional data management functions can be added as needed.
