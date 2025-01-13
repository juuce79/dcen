class MainView:
    def get_user_choice(self):
        while True:
            print("\nChoose an option:")
            print("1. Manage Names")
            print("2. Manage Addresses")
            print("3. Manage Bank Cards")
            choice = input("Enter choice (1-3): ")
            if choice in ['1', '2', '3']:
                return choice
            print("Invalid choice. Please try again.")
