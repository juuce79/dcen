import json
import os
import uuid

from models.bank_card import BankCard
from views.bank_card_view import BankCardView

DATA_DIR = "data"
CARDS_DIR = os.path.join(DATA_DIR, "cards")
CARD_MAP_FILE = os.path.join(CARDS_DIR, "card_map.json")

class BankCardController:
    def __init__(self):
        self.view = BankCardView()
        os.makedirs(CARDS_DIR, exist_ok=True)

    def _delete_existing_files(self):
        for filename in os.listdir(CARDS_DIR):
            if filename.endswith('.json') and filename != "card_map.json":
                file_path = os.path.join(CARDS_DIR, filename)
                os.remove(file_path)

    def _save_card_data(self, data):
        if not data:
            return None, None
        data_hash = str(uuid.uuid4())
        filename = f"{data_hash}.json"
        filepath = os.path.join(CARDS_DIR, filename)
        with open(filepath, 'w') as f:
            json.dump({'data': data}, f)
        return data_hash, filename

    def _load_card_map(self):
        try:
            with open(CARD_MAP_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def _save_card_map(self, card_map):
        with open(CARD_MAP_FILE, 'w') as f:
            json.dump(card_map, f, indent=4)

    def run(self):
        card_map = self._load_card_map()
        if card_map:
            if self.view.ask_show_stored():
                card = BankCard()
                card.card_number1_hash = card_map.get("card_number1")
                card.card_number2_hash = card_map.get("card_number2")
                card.card_number3_hash = card_map.get("card_number3")
                card.card_number4_hash = card_map.get("card_number4")
                card.expiry_hash = card_map.get("expiry")
                card.first_name_hash = card_map.get("first_name")
                card.middle_name_hash = card_map.get("middle_name")
                card.last_name_hash = card_map.get("last_name")
                card.cvc_hash = card_map.get("cvc")
                card.bank_name_hash = card_map.get("bank_name")
                card_details = card.get_card_details(CARDS_DIR, card_map)
                self.view.display_card(card_details)
                return

        try:
            (card_number1, card_number2, card_number3, card_number4,
             expiry, first_name, middle_name, last_name, cvc, bank_name) = self.view.get_user_input()

            if not all([card_number1, card_number2, card_number3, card_number4,
                       expiry, first_name, last_name, cvc, bank_name]):
                self.view.display_error("All fields except middle name are required.")
                return

            self._delete_existing_files()

            card_map = {}
            for name, value in [
                ("card_number1", card_number1),
                ("card_number2", card_number2),
                ("card_number3", card_number3),
                ("card_number4", card_number4),
                ("expiry", expiry),
                ("first_name", first_name),
                ("middle_name", middle_name),
                ("last_name", last_name),
                ("cvc", cvc),
                ("bank_name", bank_name)
            ]:
                if value:
                    data_hash, _ = self._save_card_data(value)
                    card_map[name] = data_hash

            self._save_card_map(card_map)

            card = BankCard(**{f"{k}_hash": v for k, v in card_map.items()})
            card_details = card.get_card_details(CARDS_DIR, card_map)
            self.view.display_card(card_details)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting...")
        except Exception as e:
            self.view.display_error(f"An unexpected error occurred: {e}")
