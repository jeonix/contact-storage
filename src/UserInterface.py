from Menu import Menu
from MenuOption import MenuOption
from ContactList import ContactList

class UserInterface:

    def __init__(self):
        self.__m_menu = Menu("Contact Menu")
        self.__m_menu += MenuOption("P", "Print Contact Menu")
        self.__m_menu += MenuOption("A", "Add a new contact")
        self.__m_menu += MenuOption("X", "Exit the program")
        self.contact_list = ContactList

    def run(self):
        while True:
            command = self.__m_menu.prompt()
            return command