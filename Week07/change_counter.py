filename = "count.txt"
def read_number() :
    with open (filename) as f:
        number = int (f.read() )
        return number
    
#TEST IT
num = read_number()
print (num)

def write_number(number):
    with open(filename, "wt") as f:
        f.write(str(number))

#test
write_number(3)

#main
num = read_number()
num += 1
print (f"we have run this program {num} times")
write_number (num)

