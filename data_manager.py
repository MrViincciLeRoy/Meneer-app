import json

# This path will be overwritten by main.py for the packaged app
DATA_FILE_PATH = 'data/subjects.json'

def load_subjects():
    """Loads the list of subjects from the JSON file."""
    try:
        with open(DATA_FILE_PATH, 'r') as f:
            data = json.load(f)
            return data.get("subjects", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return ["Default Subject"]
