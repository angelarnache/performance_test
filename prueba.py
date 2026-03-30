from register import register_user
from consult import consult_students
from look_for import search_student
from update import update_student
from delete import delete_student

listas =("1 register","2 consult","3 look for","4 update","5 delete","6 exit")

condicion = "false"
while condicion == "false":
    print("────────welcome────────")
    print("────student report─────")
    for lista in listas:
        print(lista)

    try:
        user = int(input ("Enter a number from the list: "))
        if 1 <= user <= 6:
            if user == 1:
                register_user()
            if user == 2:
                consult_students()
            if user == 3:
                search_student()
            if user == 4:
                update_student()
            if user == 5:
                delete_student()
            elif user == 6:
                print("see you later")
                break
            else:
                print("The number is unlisted")
    except ValueError:
        print("Invalid option, try the numbers in the list")