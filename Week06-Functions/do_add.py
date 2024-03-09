
students = []


def read_modules():
    modules = []
    module_name = input("Please enter the name of the module (blank to quit): ").strip()

    while module_name != "":
        module = {}
        module ["name"] = module_name
        module["grade"] = int(input("\t\t Enter grade: "))
        modules.append(module)
        
        module_name = input("\t Enter next module name (blank to quit)").strip() 

    return modules


def do_add(students):
    current_student = {}
    current_student ["name"] = input("enter name: ")
    current_student ["modules"] = read_modules()
    
    students.append(current_student)

#test
do_add(students)
do_add(students)
print (students)