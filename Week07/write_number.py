filename = "count.txt"

def write_number(number):
    with open(filename, "wt") as f:
        f.write(str(number))

#test
write_number(3)
