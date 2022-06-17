# main driver

import sys
import time
from ContactList import ContactList

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("A CSV file must be provided")
        sys.exit(1)
    else:
        csvFile = sys.argv[1]
        before = time.time()
        contacts = ContactList(csvFile=csvFile)
        contacts.contact_menu()
        after = time.time()
        end_time = after - before
        print(f"Runtime: {end_time.__round__()} seconds")
