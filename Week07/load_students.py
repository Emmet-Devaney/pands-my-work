import json
# the array we store everything in 
students= []
filename ="students.json"
def write_dict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def read_dict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty array
    # we can do this later
    with open(filename) as f:
        return json.load(f)


def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

def do_add():
    current_student = {}
    current_student["name"]=input("Enter name :")
    current_student["modules"]= read_modules()
    students.append(current_student)

def read_modules():
    modules = []
    module_name = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while module_name != "":
        module = {}
        module["name"]= module_name
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        module_name = input("\tEnter next module name (blank to quit) :").strip()

    return modules
def display_modules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}" )

def do_view():
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"]);

def do_save():
    write_dict(students)
    print("students saved")

def do_load():
    # we are changing the global variable students 
    # so we need to indicate this
    # (this stumped me for a little bit)
    global students 
    students = read_dict()
    print ("students loaded")

#main program
choice = display_menu()
while(choice != 'q'):
    # we could do this with lamda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        do_add()
    elif choice == 'v':
        do_view()
    elif choice == 's':
        do_save()
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    #print(students)
    choice=display_menu()