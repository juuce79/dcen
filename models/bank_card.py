import json
import os

class BankCard:
    def __init__(self, card_number1_hash=None, card_number2_hash=None, 
                 card_number3_hash=None, card_number4_hash=None,
                 expiry_hash=None, first_name_hash=None, 
                 middle_name_hash=None, last_name_hash=None,
                 cvc_hash=None, bank_name_hash=None):
        self.card_number1_hash = card_number1_hash
        self.card_number2_hash = card_number2_hash
        self.card_number3_hash = card_number3_hash
        self.card_number4_hash = card_number4_hash
        self.expiry_hash = expiry_hash
        self.first_name_hash = first_name_hash
        self.middle_name_hash = middle_name_hash
        self.last_name_hash = last_name_hash
        self.cvc_hash = cvc_hash
        self.bank_name_hash = bank_name_hash

    def get_card_details(self, cards_dir, card_map):
        try:
            number1 = self._load_card_data(cards_dir, self.card_number1_hash)
            number2 = self._load_card_data(cards_dir, self.card_number2_hash)
            number3 = self._load_card_data(cards_dir, self.card_number3_hash)
            number4 = self._load_card_data(cards_dir, self.card_number4_hash)
            expiry = self._load_card_data(cards_dir, self.expiry_hash)
            first = self._load_card_data(cards_dir, self.first_name_hash)
            middle = self._load_card_data(cards_dir, self.middle_name_hash) if self.middle_name_hash else ""
            last = self._load_card_data(cards_dir, self.last_name_hash)
            cvc = self._load_card_data(cards_dir, self.cvc_hash)
            bank = self._load_card_data(cards_dir, self.bank_name_hash)
            
            card_number = f"{number1} {number2} {number3} {number4}"
            name = f"{first} {middle} {last}".strip()
            
            return f"Bank: {bank}\nCard: {card_number}\nName: {name}\nExpiry: {expiry}\nCVC: {cvc}"

        except FileNotFoundError:
            return "Card data not found."
        except KeyError:
            return "Card data corrupted."

    def _load_card_data(self, data_dir, data_hash):
        if not data_hash:
            raise KeyError("Data hash is missing")
            
        filename = f"{data_hash}.json"
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r') as f:
            data = json.load(f)
            return data['data']
