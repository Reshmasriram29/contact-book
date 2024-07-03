# contact_book.py

import os

# Define the file to store contacts
CONTACTS_FILE = 'contacts.txt'

def load_contacts():
    """Load contacts from the file."""
    contacts = []
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            contacts = [line.strip() for line in file.readlines()]
    return contacts

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def add_contact(name, phone):
    """Add a new contact to the list."""
    contacts.append(f'{name},{phone}')
    save_contacts(contacts)
    print(f'Contact {name} added!')

def view_contacts():
    """Display all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("Your contacts:")
        for i, contact in enumerate(contacts, 1):
            name, phone = contact.split(',')
            print(f"{i}. {name} - {phone}")

def remove_contact(index):
    """Remove a contact from the list by its index."""
    try:
        contact = contacts.pop(index - 1)
        save_contacts(contacts)
        name, phone = contact.split(',')
        print(f'Contact {name} removed!')
    except IndexError:
        print("Invalid contact number.")

def main():
    """Main function to run the Contact Book application."""
    global contacts
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add a contact")
        print("2. View contacts")
        print("3. Remove a contact")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            view_contacts()
            try:
                index = int(input("Enter the contact number to remove: "))
                remove_contact(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the Contact Book application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
