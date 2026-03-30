from register import inventory

def search_student():
    print("──welcome to the search engine──")
    condition = "false"
    while condition == "false":
        opcion=input("Please enter a name: ")
        if opcion.isalpha():
            break
        else:
            print("Invalid option, please try again")
    if opcion in inventory["name"]:
        indication=inventory["name"].index(opcion)
        print("──student found──")
        print(f"ID:{inventory['ident'][indication]}")
        print(f"name:{inventory['name'][indication]}")
        print(f"age:{inventory['age'][indication]}")
        print(f"program:{inventory['program'][indication]}")
        print(f"state:{inventory['state'][indication]}")
    else:
        print(f"the student{indication}not exist")

