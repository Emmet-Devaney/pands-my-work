

def menu_display():
    print("What would you like to do?")
    print("/t (a) Add a new student")
    print("/t (v)View current students")
    print("/t (q)Quit")
    choice = input("Type the corresponding letter to choose: a; v; q;").strip()

    return choice


choice = menu_display
print(f"You have chosen: {choice}")

