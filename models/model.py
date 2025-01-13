class MainModel:
    def get_controller_type(self, choice):
        controller_map = {
            '1': 'name',
            '2': 'address',
            '3': 'card'
        }
        return controller_map.get(choice)
