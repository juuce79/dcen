import json
import os
import uuid

from models.name import Person
from views.name_view import NameView

DATA_DIR = "data"
NAMES_DIR = os.path.join(DATA_DIR, "names")
NAME_MAP_FILE = os.path.join(NAMES_DIR, "name_map.json")

class NameController:
    def __init__(self):
        self.view = NameView()
        os.makedirs(NAMES_DIR, exist_ok=True)

    def _delete_existing_files(self):
        for filename in os.listdir(NAMES_DIR):
            if filename.endswith('.json') and filename != "name_map.json":
                file_path = os.path.join(NAMES_DIR, filename)
                os.remove(file_path)

    def _save_name(self, name):
        if not name:
            return None, None
        name_hash = str(uuid.uuid4())
        filename = f"{name_hash}.json"
        filepath = os.path.join(NAMES_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump({'name': name}, f)
        return name_hash, filename

    def _load_name_map(self):
        try:
            with open(NAME_MAP_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_name_map(self, name_map):
        with open(NAME_MAP_FILE, 'w') as f:
            json.dump(name_map, f, indent=4)

    def run(self):
        name_map = self._load_name_map()
        if name_map:
            if self.view.ask_show_stored():
                person = Person()
                person.first_name_hash = name_map.get("first")
                person.middle_name_hash = name_map.get("middle")
                person.last_name_hash = name_map.get("last")
                full_name = person.get_full_name(NAMES_DIR, name_map)
                self.view.display_full_name(full_name)
                return

        try:
            first, middle, last = self.view.get_user_input()
            if not first or not last:
                self.view.display_error("First and last names are required.")
                return

            self._delete_existing_files()  # Delete existing files before saving new ones

            first_hash, first_filename = self._save_name(first)
            last_hash, last_filename = self._save_name(last)
            middle_hash, middle_filename = self._save_name(middle) if middle else (None, None)

            name_map = {}  # Reset name_map
            name_map["first"] = first_hash
            name_map["last"] = last_hash
            if middle_hash:
                name_map["middle"] = middle_hash
            self._save_name_map(name_map)

            person = Person(first_hash, middle_hash, last_hash)
            full_name = person.get_full_name(NAMES_DIR, name_map)
            self.view.display_full_name(full_name)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
        except Exception as e:
            self.view.display_error(f"An unexpected error occurred: {e}")
