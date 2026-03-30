from register import inventory

condition = "false"
def update_student():
    if len(inventory["ident"])==0:
        print("The list is empty")
        return
    
    print("──students──")
    for i in range(len(inventory["ident"])):
        print(f"{i+1} ID:{inventory['ident'][i]}-name:{inventory['name'][i]}- age:{inventory['age'][i]}-program:{inventory['program'][i]}-state:{inventory['state'][i]}")
        print("─────────────\n")

        while condition == "false":
            try:
                indication=int(input("Enter the student number to update: "))-1
                if 0<= indication<len(inventory["ident"]):
                    break
                else:
                    print("Invalid number, please try again")
            except ValueError:
                print("Invalid option, please try again")
    
    print(f"\nselected student: {inventory['name'][indication]}")
    print("If you do not wish to change an option, just press ENTER\n")

    new_id=input(f"actual_ID '{inventory['ident'][indication]}',New_ID: ")
    if new_id.strip()== "":
        pass
    else:
        try:
            inventory["ident"][indication] = int(new_id)
        except ValueError:
            print("Invalid amount will remain the same")

    new_name=input(f"actual_name '{inventory['name'][indication]}',New_ID: ")
    if new_name.strip()== "":
        pass
    elif new_name.isalpha():
        inventory["name"][indication]=new_name
    else:
        print("Invalid name will be left as is")

    new_age=input(f"actual_age'{inventory['age'][indication]}',New_age: ")
    if new_age.strip()== "":
        pass
    else:
        try:
            inventory["age"][indication] = int(new_age)
        except ValueError:
            print("Invalid amount will remain the same")

    new_program=input(f"actual_program '{inventory['program'][indication]}',New_program: ")
    if new_program.strip()== "":
        pass
    elif new_program.isalpha():
        inventory["program"][indication]=new_program
    else:
        print("Invalid program will be left as is")

    new_state=input(f"actual_state '{inventory['state'][indication]}',New_state: ")
    if new_state.strip()== "":
        pass
    elif new_state.isalpha():
        inventory["state"][indication]=new_state
    else:
        print("Invalid state, please try again")

    print(f"ID: {inventory['ident'][indication]}")
    print(f"name: {inventory['name'][indication]}")
    print(f"age: {inventory['age'][indication]}")
    print(f"program: {inventory['program'][indication]}")
    print(f"state: {inventory['state'][indication]}")
