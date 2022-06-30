# Contact Storage
A simple program that uses python dictionaries and CSV files. I'm taking a brute-force type of approach as in not using
CSV-specific libraries and related methods. The aim is to help me learn with working with data and fine-tuning a user-friendly
interface.
- I wrote the CSV file myself which restricts the program in what specific data each column can be interpreted
- The `Menu.py` and `MenuOption.py` classes are based off a separate program that I wrote for an assignment in one of my college courses
  and I understand most of the functionality but am not completely sure if they are necessary to use for this program
- I attempted to use Tkinter for better UI but couldn't decide if a GUI could be interacted with from the command line in real time so the idea was scrapped

## Instructions
- On the command line run the `cd` command to go to the contact-storage directory
- The run the command `python src/main.py data/ExampleContacts.csv`
- The contact menu will be presented in the shell with several options the user can pick from

## System Design

###`ContactList.py`
  - Imports `Menu`, `MenuOption`
  - Class Constructor Data Members:
    - csvFile: A user-provided CSV file containing data of contacts and is the only argument for the constructor
    - friendDict: Python Dictionary that the CSV file is interpreted into that are categorized as "friends"
    - familyDict: Python Dictionary that the CSV file is interpreted into that are categorized as "family"
    - `dictate()`: method that is called when a ContactList object is initialized
  - Methods:
    - `__read_file(self)`:
      - Checks to see if a valid file is provided in the class constructor
      - Uses built-in Python function to open the file and reads through it
      - Closes the file and returns it
    - `get_friend_dict(self)`:
      - returns friendDict
    - `get_family_dict(self)`:
      - returns familyDict
    - `dictate(self)`:
      - Calls `self.__read_file()` to retrieve a valid file and assigns it to the variable `file`
      - `file` is looped through and each line in the file is made into a list separated by commas that goes by the variable `contactType`
      - Then a check is done to see whether the third column is categorized as "friend" or "family"
      - Depending on the check, the name of the contact is made into a key of a nested dictionary of one of the two class attributed dictionaries
        - The data in each column are made into the value of the nested dictionary
    - `print_dictionary(self)`:
      - The User is prompted to input which of the two dictionaries they want to view
      - Depending on the user's input, the key and value of each contact is printed
    - `add_contact(self)`:
      - The user is prompted to input which type of relationship the contact to be added falls under
      - Depending on the relationship, the user inputs name, id number, job title, and birthdate
      - The new contact is added as a nested dictionary in the dictionary
    - `delete_contact(self)`:
      - The user is prompted to input which type of relationship the contact to be deleted falls under
      - The user is prompted to input the name of the contact to be deleted
      - The user is prompted to confirm they want to delete the contact found
      - A message is displayed a message confirming the contact was removed
    - `find_contact(self)`:
      - The user is prompted to enter the contact's name that they are looking for
      - If the name of the contact is found in either dictionary, the information for that contact is displayed
      - If the name of the contact isn't found, the user is notified and returned to the menu
    - `yes_or_no(self)`:
      - User is prompted to answer yes or no
      - If the user answers yes then the method returns True
      - If the user answers no then the method returns False