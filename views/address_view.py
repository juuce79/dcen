class AddressView:
    def ask_show_stored(self):
        while True:
            choice = input("Do you want to show the stored address? (y/n): ").lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def get_user_input(self):
        street = input("Enter street address: ")
        city = input("Enter city: ")
        state = input("Enter state: ")
        zip_code = input("Enter ZIP code: ")
        return street, city, state, zip_code

    def display_address(self, address):
        print(f"Address: {address}")

    def display_error(self, message):
        print(f"Error: {message}")
