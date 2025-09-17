def display_menu():     
    print("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit""")

def add_contact(contact_book):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address,
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    dict_name = input("Enter name to view: ")
    if dict_name in contact_book:
        print("Name:", dict_name)
        print("Phone:", contact_book[dict_name]["phone"])
        print("Email:", contact_book[dict_name]["email"])
        print("Address:", contact_book[dict_name]["address"])
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    edit_name = input("Enter name to edit: ")
    if edit_name in contact_book:
        edit_phone = input("Enter new phone (leave blank to keep current): ")
        edit_email = input("Enter new email (leave blank to keep current): ")
        edit_address = input("Enter new address (leave blank to keep current): ")
        if edit_phone != "":
            contact_book[edit_name]["phone"] = edit_phone
        if edit_email != "":
            contact_book[edit_name]["email"] = edit_email
        if edit_address != "":
            contact_book[edit_name]["address"] = edit_address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    dlt_name = input("Enter name to delete: ")
    if dlt_name in contact_book:
        contact_book.pop(dlt_name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print("Name:", name)
            print("Phone:", details["phone"])
            print("Email:", details["email"])
            print("Address:", details["address"])
            print()

# Main Program
contact_book = {}

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        add_contact(contact_book)
    elif choice == 2:
        view_contact(contact_book)
    elif choice == 3:
        edit_contact(contact_book)
    elif choice == 4:
        delete_contact(contact_book)
    elif choice == 5:
        list_all_contacts(contact_book)
    elif choice == 6:
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
