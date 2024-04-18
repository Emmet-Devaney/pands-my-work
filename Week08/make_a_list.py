# This is just to show you numpy exists
# Author: Andrew Beatty

import numpy as np

min_salary= 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) # this is so that the "random" numbers are the same each time to make it easier to debug.
salaries = np.random.randint(min_salary, max_salary,number_of_entries)
print (salaries)

# add 5000 to each entry
salaries_plus = salaries + 5000
print(salaries_plus)

# you can also multiply 
salaries_mult = salaries * 1.05 # add 5% by mulitplying by 1.05
print(salaries_mult)
# this is a float array to convert to an int array
new_salaries = salaries_mult.astype(int)
print(new_salaries)