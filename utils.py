# --- Utility Functions for the Wisdom Tech Timeline 2025 Project ---
# This file contains helper functions that can be used across the entire project.

import datetime
import yaml
import logging

def get_current_timestamp():
    """Returns the current time as a formatted string."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_yaml_file(file_path):
    """
    Safely loads a YAML file and returns its content as a Python dictionary.
    Returns None if the file is not found or cannot be parsed.
    """
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
            logging.info(f"Successfully loaded YAML file: {file_path}")
            return data
    except FileNotFoundError:
        logging.error(f"YAML file not found at path: {file_path}")
        return None
    except yaml.YAMLError as e:
        logging.error(f"Error parsing YAML file {file_path}: {e}")
        return None

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Returns 0 if the list is empty to avoid division by zero errors.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def format_data_for_logging(data_dict):
    """Formats a dictionary into a human-readable string for logging."""
    if not isinstance(data_dict, dict):
        return str(data_dict)
    
    formatted_items = [f"{key.replace('_', ' ').capitalize()}: {value}" for key, value in data_dict.items()]
    return ", ".join(formatted_items)

# --- Example Usage (this part will not run when imported) ---
if __name__ == "__main__":
    print("--- Testing Utility Functions ---")

    # Test timestamp
    print(f"Current Timestamp: {get_current_timestamp()}")

    # Test list average
    my_numbers = [10, 20, 30, 40, 50]
    avg = calculate_average(my_numbers)
    print(f"The average of {my_numbers} is: {avg}")

    # Test data formatting
    sensor_data = {
        "temperature_celsius": 22.5,
        "humidity_percent": 55.0,
        "air_quality_index": 30.0
    }
    log_message = format_data_for_logging(sensor_data)
    print(f"Formatted log message: {log_message}")

    print("\n--- All utility functions seem to be working. ---")


