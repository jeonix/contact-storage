class Menu:
    def __init__(self, header):
        self.header = header
        self.__m_options = []

    def __iadd__(self, option):
        self.__m_options.append(option)
