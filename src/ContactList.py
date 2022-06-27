from Menu import Menu
from MenuOption import MenuOption

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

    def get_friend_dict(self):
        return self.friendDict

    def get_family_dict(self):
        return self.familyDict

    def dictate(self):
        file = self.__read_file()
        for line in file:
            contactType = line.rstrip().split(',')
            if contactType[2].replace('"', "") == 'friend':
                self.friendDict[contactType[0].replace('"', "")] = {}
                self.friendDict[contactType[0].replace('"', "")]['id number'] = contactType[1].replace('"', "")
                self.friendDict[contactType[0].replace('"', "")]['relationship'] = contactType[2].replace('"', "")
                self.friendDict[contactType[0].replace('"', "")]['job title'] = contactType[3].replace('"', "")
                self.friendDict[contactType[0].replace('"', "")]['birthdate'] = contactType[4].replace('"', "")
            elif contactType[2].replace('"', "") == 'family':
                self.familyDict[contactType[0].replace('"', "")] = {}
                self.familyDict[contactType[0].replace('"', "")]['id number'] = contactType[1].replace('"', "")
                self.familyDict[contactType[0].replace('"', "")]['relationship'] = contactType[2].replace('"', "")
                self.familyDict[contactType[0].replace('"', "")]['job title'] = contactType[3].replace('"', "")
                self.familyDict[contactType[0].replace('"', "")]['birthdate'] = contactType[4].replace('"', "")

    def print_dictionary(self):
        dictionary = input("Which contact list would you like? (friend or family): ")
        if dictionary.lower() == "friend":
            for key in self.friendDict:
                print(f"{key} : {self.friendDict.get(key)}")
        elif dictionary.lower() == "family":
            for key in self.familyDict:
                print(f"{key} : {self.familyDict.get(key)}")
        print()

    def add_contact(self):
        contact = input("What relationship type is the new contact? (friend or family): ")
        if contact.lower() == "friend":
            friend = input("Enter the name of the friend: ")
            friend_id = input("Enter three digit id number: ")
            job_title = input("Enter friend's job title: ")
            birthdate = input("Enter friend's birthdate in format MONTH_DAY: ")
            self.friendDict[friend]['id_number'] = friend_id
            self.friendDict[friend]['relationship'] = 'friend'
            self.friendDict[friend]['job_title'] = job_title
            self.friendDict[friend]['birthdate'] = birthdate
        elif contact.lower() == "family":
            family = input("Enter the name of the family: ")
            family_id = input("Enter three digit id number: ")
            job_title = input("Enter family's job title: ")
            birthdate = input("Enter family's birthdate in format MONTH_DAY: ")
            self.familyDict[family]['id_number'] = family_id
            self.familyDict[family]['relationship'] = 'family'
            self.familyDict[family]['job_title'] = job_title
            self.familyDict[family]['birthdate'] = birthdate
        print()

    def delete_contact(self):
        contact = input("Is the contact to be deleted friend or family? ")
        if contact.lower() == "friend":
            friend = input("What is the contact's name? ")
            if friend in self.friendDict:
                print(f"Are you sure you want to delete {friend}?")
                if self.yes_or_no():
                    self.friendDict.pop(friend)
                    print(f"{friend} has been deleted")
                else:
                    return
            else:
                print(f"{friend} not found")
                return
        elif contact.lower() == 'family':
            family = input("What is the contact's name? ")
            if family in self.familyDict:
                print(f"Are you sure you want to delete {family}?")
                if self.yes_or_no():
                    self.friendDict.pop(family)
                    print(f"{family} has been deleted")
                else:
                    return
            else:
                print(f"{family} not found")
                return
        print()

    def find_contact(self):
        contact = input("What is the contact's name you are looking for? ")
        if contact in self.friendDict.keys():
            print(f"{contact} : {self.friendDict.get(contact)}")
        elif contact in self.familyDict.keys():
            print(f"{contact} : {self.familyDict.get(contact)}")
        else:
            print(f"{contact} was not found")
        print()

    def yes_or_no(self) -> bool:
        answer = input("Yes/No? : ")
        if answer.lower().rstrip() == 'yes':
            return True
        elif answer.lower().rstrip() == 'no':
            return False

    def contact_menu(self):
        menu = Menu("Contact Menu")
        menu += MenuOption("P", "Print Contacts")
        menu += MenuOption("A", "Add a new contact")
        menu += MenuOption("D", "Delete a contact")
        menu += MenuOption("L", "Look up a contact")
        menu += MenuOption("X", "Exit the program")

        while True:
            command = menu.prompt()
            if command.upper() == 'P':
                self.print_dictionary()
                continue
            elif command.upper() == 'A':
                self.add_contact()
                continue
            elif command.upper() == 'D':
                self.delete_contact()
                continue
            elif command.upper() == 'L':
                self.find_contact()
                continue
            elif command.upper() == 'X':
                print("Thank you for using the contact menu")
                break
