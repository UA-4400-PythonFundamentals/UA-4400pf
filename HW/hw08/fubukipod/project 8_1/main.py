import os
from utils import *
from models import *

LOG_FILE = 'app.log'

def load_from_log():
    created = []
    if not os.path.exists(LOG_FILE):
        return created

    with open(LOG_FILE, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if 'User created:' in line:
                name = line.split('User created:')[1].strip()
                if not any(o['name']==name and o['role']=='user' for o in created):
                    created.append({'name': name, 'role': 'user'})
            elif 'Admin created:' in line:
                name = line.split('Admin created:')[1].strip()
                if not any(o['name']==name and o['role']=='admin' for o in created):
                    created.append({'name': name, 'role': 'admin'})
    return created

def main():
    created = load_from_log()

    print("=== Simple User/Admin Manager ===")
    while True:
        choice = input("[u]ser, [a]dmin, [l]ist, [q]uit: ").strip().lower()

        if choice == 'u':
            name = input("Enter user name: ").strip()
            if any(o['name']==name and o['role']=='user' for o in created):
                print(f"User «{name}» already exists. Skipping.")
                log_in_file(f"Duplicate user attempt: {name}")
                continue
            u = create_user(name)
            created.append(u)

        elif choice == 'a':
            name = input("Enter admin name: ").strip()
            if any(o['name']==name and o['role']=='admin' for o in created):
                print(f"Admin «{name}» already exists. Skipping.")
                log_in_file(f"Duplicate admin attempt: {name}")
                continue
            a = create_admin(name)
            created.append(a)

        elif choice == 'l':
            if not created:
                print("No users or admins created yet.")
            else:
                print("=== Created Entities ===")
                for idx, obj in enumerate(created, start=1):
                    print(f"{idx}. {obj['role'].title()}: {obj['name']}")

        elif choice == 'q':
            print("Goodbye!")
            break

        else:
            print("Unknown option. Try again.")

if __name__ == '__main__':
    main()