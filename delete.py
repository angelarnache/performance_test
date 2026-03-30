from register import inventory

condition="false"
def delete_student():
    if len(inventory["ident"])==0:
        print("The list is empty")
        return

    print("──delete_students──")
    for i in range(len(inventory["ident"])):
        print(f"{i+1} ID:{inventory['ident'][i]}-name:{inventory['name'][i]}- age:{inventory['age'][i]}-program:{inventory['program'][i]}-state:{inventory['state'][i]}")
        print("─────────────\n")
    
    while condition == "false":
        try:
            indication=int(input("Enter the number from the list you want to delete: "))-1
            if 0<= indication <len(inventory["ident"]):
                break
            else:
                print("Invalid number, please try again")
        except ValueError:
            print("")

    ident=inventory["ident"][indication]
    while condition == "false":
        confirmation=input(f"Are you sure you want to delete? yes/no: ").lower()
        if confirmation == "yes" or confirmation == "y":
            inventory["ident"].pop(indication)
            inventory["name"].pop(indication)
            inventory["age"].pop(indication)
            inventory["program"].pop(indication)
            inventory["state"].pop(indication)
            print(f"The student has been deleted")
            break
        elif confirmation == "no" or confirmation == "n":
            print("canceled delete")
            break
        else:
            print("Invalid option, please try again")



