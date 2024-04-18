students= []
def display_menu():
 
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) Save students")
    print("\t(q) Quit")
    choice = input("type one letter (a/v/s/q):").strip()
    
    return choice

def do_add(students):
    # you have code here to add
    print("in adding")

def do_view(students):
    # you have code here to view
    print("in viewing")

def do_save(students):
    #you will put the call to save dict here
    print("in save")

#main program
choice = display_menu()
while(choice != 'q'):
     # we could do this with lamda functions
     # I am keeping this basic for the moment
 if choice == 'a':
    do_add(students)
 elif choice == 'v':
    do_view(students)
 elif choice == 's':
    do_save(students)
 elif choice !='q':
    print("\n\nPlease select either a,v,s or q")
 choice = display_menu()