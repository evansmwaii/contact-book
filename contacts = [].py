contacts = []

def show_menu():
    print("\n📞 Contact Book")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Search contact")
    print("4. Edit contact")
    print("5. Delete contact")
    print("6. Exit")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone: ")
    email = input("Enter contact email (optional): ")   
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added.")

def search_contact():
    search_name = input("Enter name to search: ")
    found_contacts = [c for c in contacts if search_name.lower() in c['name'].lower()]
    
    if not found_contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(found_contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def edit_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        
        name = input("Enter new name (leave blank to keep current): ")
        phone = input("Enter new phone (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")

        if name:
            contacts[index]['name'] = name
        if phone:
            contacts[index]['phone'] = phone
        if email:
            contacts[index]['email'] = email

        print(f"Contact {index + 1} updated.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid contact number.")
            return
        
        deleted_contact = contacts.pop(index)
        print(f"Contact {deleted_contact['name']} deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()                               


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
         view_contacts()
    elif choice == "2":
         add_contact()
    elif choice == "3":
         search_contact()
    elif choice == "4":
         edit_contact()
    elif choice == "5":
         delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
