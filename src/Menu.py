from ContactList import ContactList

class Menu:
    def __init__(self, header):
        self.header = header
        self.__m_options = []
        print(f"\n{header}")

    def __iadd__(self, option):
        self.__m_options.append(option)
        return self

    def __len__(self):
        return len(self.__m_options)

    def __getitem__(self, nIdx):
        if 0 <= nIdx < len(self):
            return self.__m_options[nIdx]
        else:
            raise IndexError

    def __is_valid_command(self, command):
        for i in range(len(self)):
            if command.upper() == self[i].command().upper():
                return True
        return False

    def menu_option(self, command, description):
        print(f"{command}: {description}")

    def prompt(self):
        while True:
            options = []

            for i in range(len(self)):
                option = self[i]
                if option is not None:
                    options += option.command()

            command = input("Please enter a command: ")
            if self.__is_valid_command(command):
                return command
            else:
                print("Please enter one of the letter commands")
                return
