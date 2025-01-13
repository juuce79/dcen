from controllers.name_controller import NameController
from controllers.address_controller import AddressController
from controllers.bank_card_controller import BankCardController
from models.model import MainModel
from views.view import MainView

class MainController:
    def __init__(self):
        self.view = MainView()
        self.model = MainModel()
        self.controllers = {
            'name': NameController,
            'address': AddressController,
            'card': BankCardController
        }

    def run(self):
        choice = self.view.get_user_choice()
        controller_type = self.model.get_controller_type(choice)
        controller = self.controllers[controller_type]()
        controller.run()
