#app.py
from d_operations import create_table, create_user, get_user, update_user, delete_user

def menu():
    print("=== User Management System ===")
    print("1. Create user")
    print("2. View User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

create_table()  #ensure the table exists

while True:
    menu()
    choice =input("enter your choice:")

    match choice:
        case '1':
            name =input("Enter name:")
            email = input("Enter email")
            create_user(name,email)

        case '2':
            print("User list:")
            get_user()

        case '3':
            user_id = int(input("Enter user ID to update:"))
            new_name= input("Enter new name")
            new_email= input("Enter new email:")
            update_user (user_id, new_name, new_email)

        case '4':
            user_id =int(input("Enter user ID to delete:"))
            delete_user(user_id)

        case '5':
            print("\nproject Terminated")
            break
        
        case _:
            print("\n Invalid choice , please try again")







