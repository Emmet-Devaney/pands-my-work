
def menu_display():
    print("What would you like to do?")
    print("/t (a) Add a new student")
    print("/t (v) View current students")
    print("/t (q) Quit")
    choice = input("Type the corresponding letter to choose: a; v; q;").strip()

    return choice

def do_add():

    print("in adding")


def do_view():

    print("in viewing")


choice = menu_display
while (choice != "q"):

    if choice == "a":
        do_add()
    elif choice == "v":
        do_view()
    elif choice != "q":
        print ("\n\n please select either a; v; q.")
    choice = menu_display()

