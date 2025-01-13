import json
import os
import uuid

from models.address import Address
from views.address_view import AddressView

DATA_DIR = "data"
ADDRESSES_DIR = os.path.join(DATA_DIR, "addresses")
ADDRESS_MAP_FILE = os.path.join(ADDRESSES_DIR, "address_map.json")

class AddressController:
    def __init__(self):
        self.view = AddressView()
        os.makedirs(ADDRESSES_DIR, exist_ok=True)

    def _delete_existing_files(self):
        for filename in os.listdir(ADDRESSES_DIR):
            if filename.endswith('.json') and filename != "address_map.json":
                file_path = os.path.join(ADDRESSES_DIR, filename)
                os.remove(file_path)

    def _save_address(self, address_part):
        if not address_part:
            return None, None
        address_hash = str(uuid.uuid4())
        filename = f"{address_hash}.json"
        filepath = os.path.join(ADDRESSES_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump({'address': address_part}, f)
        return address_hash, filename

    def _load_address_map(self):
        try:
            with open(ADDRESS_MAP_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_address_map(self, address_map):
        with open(ADDRESS_MAP_FILE, 'w') as f:
            json.dump(address_map, f, indent=4)

    def run(self):
        address_map = self._load_address_map()
        if address_map:
            if self.view.ask_show_stored():
                address = Address()
                address.street_hash = address_map.get("street")
                address.city_hash = address_map.get("city")
                address.state_hash = address_map.get("state")
                address.zip_hash = address_map.get("zip")
                full_address = address.get_full_address(ADDRESSES_DIR, address_map)
                self.view.display_address(full_address)
                return

        try:
            street, city, state, zip_code = self.view.get_user_input()
            if not all([street, city, state, zip_code]):
                self.view.display_error("All address fields are required.")
                return

            self._delete_existing_files()

            street_hash, _ = self._save_address(street)
            city_hash, _ = self._save_address(city)
            state_hash, _ = self._save_address(state)
            zip_hash, _ = self._save_address(zip_code)

            address_map = {}
            address_map["street"] = street_hash
            address_map["city"] = city_hash
            address_map["state"] = state_hash
            address_map["zip"] = zip_hash
            self._save_address_map(address_map)

            address = Address(street_hash, city_hash, state_hash, zip_hash)
            full_address = address.get_full_address(ADDRESSES_DIR, address_map)
            self.view.display_address(full_address)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
        except Exception as e:
            self.view.display_error(f"An unexpected error occurred: {e}")
