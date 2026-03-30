from register import inventory

def consult_students():
    if len(inventory["ident"])==0:
        print("The list is empty")

    else:
        print("\n──welcome to consult──")
        for i in range(len(inventory["ident"])):
            print(f"student {i+1}:")
            print(f"ID:{inventory['ident'][i]}")
            print(f"name:{inventory['name'][i]}")
            print(f"age:{inventory['age'][i]}")
            print(f"program:{inventory['program'][i]}")
            print(f"state:{inventory['state'][i]}")
    print("────────────────\n")