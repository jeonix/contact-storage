class ContactList:
    def __init__(self, csvFile=None):
        self.csvFile = csvFile
        self.friendDict = {}
        self.familyDict = {}
        self.dictate()

    def __read_file(self):
        if self.csvFile is not None:
            with open(self.csvFile) as openFile:
                openFile.readline()  # discard the column labels
                file = openFile.readlines()
                openFile.close()
            return file
        else:
            print("Invalid input")

    def dictate(self):
        file = self.__read_file()
        for line in file:
            contactType = line.rstrip().split(',')
            if contactType[2].replace('"', "") == 'friend':
                self.friendDict[contactType[0].replace('"', "")] = contactType[1].replace('"', "")
            elif contactType[2].replace('"', "") == 'family':
                self.familyDict[contactType[0].replace('"', "")] = contactType[1].replace('"', "")

    def print_dictionary(self):
        dictionary = input("Which contact list would you like? (friend or family): ")
        if dictionary.lower() == "friend":
            for key in self.friendDict:
                print(f"{key}'s id number: {self.friendDict.get(key)}")
        elif dictionary.lower() == "family":
            for key in self.familyDict:
                print(f"{key}'s id number: {self.familyDict.get(key)}")

    def add_contact(self):
        contact = input("What relationship type is the new contact? (friend or family): ")
        if contact.lower() == "friend":
            friend = input("Enter the name of the friend: ")
            friend_id = input("Enter three digit id number : ")
            self.friendDict[friend] = friend_id
        elif contact.lower() == "family":
            family = input("Enter the name of the family: ")
            family_id = input("Enter three digit id number")
            self.familyDict[family] = family_id