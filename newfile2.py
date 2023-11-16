class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = Contact(name, phone_number, email, address)
    contacts.append(contact)
    print("Contact added!")

def view_contact_list():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone_number}")

def search_contact(query):
    results = []
    for contact in contacts:
        if query.lower() in contact.name.lower() or query in contact.phone_number:
            results.append(contact)
    
    if not results:
        print("No matching contacts found.")
    else:
        print("Matching contacts:")
        for i, result in enumerate(results):
            print(f"{i + 1}. Name: {result.name}, Phone: {result.phone_number}")

def update_contact(index):
    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"Editing contact: {contact.name}")
        contact.name = input("Enter new name: ")
        contact.phone_number = input("Enter new phone number: ")
        contact.email = input("Enter new email: ")
        contact.address = input("Enter new address: ")
        print("Contact updated!")
    else:
        print("Invalid contact index!")

def delete_contact(index):
    if 0 <= index < len(contacts):
        del contacts[index]
        print("Contact deleted!")
    else:
        print("Invalid contact index!")

def main():
    while True:
        print("\nCONTACT MANAGEMENT MENU:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            index = int(input("Enter contact index to update: "))
            update_contact(index - 1)
        elif choice == '5':
            index = int(input("Enter contact index to delete: "))
            delete_contact(index - 1)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()