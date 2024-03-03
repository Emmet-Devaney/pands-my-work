


student = {
    "name" : "Mary",
    "modules": [
        {
            "course name" : "Programming",
            "grade" : 45
        },
        {
            "course name" : "History",
            "grade" : 99
        }
    ]
}

print ("student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["course name"], module["grade"]))

'''
Extra
5. Write a program that will read in the data for the data structure above, ie 
reads in a student’s name, then keeps reading in their modules and grades
(until the user enters a blank module name), 
You can break this up into two parts:
a. Just read in the module names until the user enters blank,
b. Then read in the grade as well
This program can just read in one student (and their module details).
6. If you want to go a step further, read in multiple students (until the 
student_name is blank. 
Next week we will be looking at functions and we will implement something 
like this.
'''