import json
from pathlib import Path

# Create a dummy data file for the example
DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)
subjects_file = DATA_DIR / "subjects.json"
if not subjects_file.exists():
    with open(subjects_file, 'w') as f:
        json.dump({"subjects": ["Mathematics", "Science", "History"]}, f)

def load_subjects():
    """Loads the list of subjects from the JSON file."""
    try:
        with open(subjects_file, 'r') as f:
            data = json.load(f)
            return data.get("subjects", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return ["Default Subject"]
