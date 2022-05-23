# main driver

import sys
import time
from ContactList import ContactList

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("A CSV file must be provided")
        sys.exit(1)
    else:
        csvFile = sys.argv[1]
        before = time.time()
        contacts = ContactList(csvFile=csvFile)
        contacts.print_dictionary()
