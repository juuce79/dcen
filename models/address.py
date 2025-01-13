import json
import os

class Address:
    def __init__(self, street_hash=None, city_hash=None, state_hash=None, zip_hash=None):
        self.street_hash = street_hash
        self.city_hash = city_hash
        self.state_hash = state_hash
        self.zip_hash = zip_hash

    def get_full_address(self, addresses_dir, address_map):
        try:
            street = self._load_address(addresses_dir, self.street_hash)
            city = self._load_address(addresses_dir, self.city_hash)
            state = self._load_address(addresses_dir, self.state_hash)
            zip_code = self._load_address(addresses_dir, self.zip_hash)
            
            return f"{street}\n{city}, {state} {zip_code}"

        except FileNotFoundError:
            return "Address data not found."
        except KeyError:
            return "Address data corrupted."

    def _load_address(self, data_dir, address_hash):
        if not address_hash:
            raise KeyError("Address hash is missing")
            
        filename = f"{address_hash}.json"
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data['address']
