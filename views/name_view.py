class NameView:
    def ask_show_stored(self):
        while True:
            choice = input("Do you want to show the stored name? (y/n): ").lower()
            if choice in ('y', 'n'):
                return choice == 'y'
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def get_user_input(self):
        first_name = input("Enter first name: ")
        middle_name = input("Enter middle name (optional): ")
        last_name = input("Enter last name: ")
        return first_name, middle_name, last_name

    def display_full_name(self, full_name):
        print(f"Full name: {full_name}")

    def display_error(self, message):
        print(f"Error: {message}")
