inventory={"ident":[],
"name":[],
"age":[],
"program":[],
"state":[]}


condicion="false"
def register_user():
    print("──welcome to registre──")
    while condicion == "false":
        while condicion == "false":
            try:
                opcion=(int(input("Register the ID: ")))
                print("save")
                inventory["ident"].append(opcion)
                break
            except ValueError:
                print("Please try again. Enter only whole numbers.")
        
        while condicion == "false":
            opcion_2=input("Please enter the name: ")
            if opcion_2.isalpha():
                print("save")
                inventory["name"].append(opcion_2)
                break
            else:
                print("Invalid option, please try again")

        while condicion == "false":
            try:
                opcion_3=(int(input("Register the age: ")))
                print("save")
                inventory["age"].append(opcion_3)
                break
            except ValueError:
                print("Please try again. Enter only whole numbers.")

        while condicion == "false":
            opcion_4=input("Please enter the program: ")
            if opcion_4.isalpha():
                print("save")
                inventory["program"].append(opcion_4)
                break
            else:
                print("Invalid option, please try again")

        while condicion == "false":
            opcion_6=input("Please enter the state: ")
            if opcion_6.isalpha():
                print("save")
                inventory["state"].append(opcion_6)
                break
            else:
                print("Invalid option, please try again")

        opcion_5 = input("Do you want to add more products? yes/no: ").lower()
        if opcion_5 == "yes" or opcion_5 == "y":
            continue
        elif opcion_5 == "no" or opcion_5 == "no":
            return
        else:
            print("invalid option")

