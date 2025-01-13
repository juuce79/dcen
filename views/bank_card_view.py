class BankCardView:
    def ask_show_stored(self):
        while True:
            choice = input("Do you want to show the stored card? (y/n): ").lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def get_user_input(self):
        print("\nEnter card number in groups of 4 digits:")
        card_number1 = input("First 4 digits: ")
        card_number2 = input("Second 4 digits: ")
        card_number3 = input("Third 4 digits: ")
        card_number4 = input("Last 4 digits: ")
        expiry = input("Expiry date (MM/YY): ")
        first_name = input("First name: ")
        middle_name = input("Middle name (optional): ")
        last_name = input("Last name: ")
        cvc = input("CVC: ")
        bank_name = input("Bank name: ")
        return (card_number1, card_number2, card_number3, card_number4, 
                expiry, first_name, middle_name, last_name, cvc, bank_name)

    def display_card(self, card_details):
        print(f"\nCard Details:\n{card_details}")

    def display_error(self, message):
        print(f"Error: {message}")
