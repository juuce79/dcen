import json
import os

class Person:
    def __init__(self, first_name_hash=None, middle_name_hash=None, last_name_hash=None):
        self.first_name_hash = first_name_hash
        self.middle_name_hash = middle_name_hash
        self.last_name_hash = last_name_hash

    def get_full_name(self, names_dir, name_map):
        try:
            first = self._load_name(names_dir, self.first_name_hash)
            last = self._load_name(names_dir, self.last_name_hash)
            middle = self._load_name(names_dir, self.middle_name_hash) if self.middle_name_hash else ""
            
            if middle:
                return f"{first} {middle} {last}"
            return f"{first} {last}"

        except FileNotFoundError:
            return "Name data not found."
        except KeyError:
            return "Name data corrupted."

    def _load_name(self, data_dir, name_hash):
        if not name_hash:
            raise KeyError("Name hash is missing")
            
        filename = f"{name_hash}.json"
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data['name']
