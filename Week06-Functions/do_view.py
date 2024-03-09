

def menu_display():
    print("What would you like to do?")
    print("/t (a) Add a new student")
    print("/t (v) View current students")
    print("/t (q) Quit")
    choice = input("Type the corresponding letter to choose: a; v; q; : ").strip()

    return choice

def do_add(students):
    current_student = {}
    current_student ["name"] = input("enter name: ")
    current_student ["modules"] = read_modules()
    
    students.append(current_student)


def read_modules():
    modules = []
    module_name = input("Please enter the name of the module (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module ["name"] = module_name
        module["grade"] = int(input("\t\t Enter grade: "))
        modules.append(module)
        
        module_name = input("\t Enter next module name (blank to quit): ").strip() 

    return modules

def display_modules(modules):
    print("\t name:  \t grade: ")
    for module in modules:
        print(f"\t {module['name']}     \t {module['grade']}")



def do_view(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])
    print(students)

students = []

choice = menu_display()
while (choice != "q"):

    if choice == "a":
        do_add(students)
    elif choice == "v":
        do_view(students)
    elif choice != "q":
        print ("\n\n please select either a; v; q.")
    choice = menu_display()