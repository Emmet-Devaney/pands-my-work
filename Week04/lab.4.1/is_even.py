#the user to enter in a number, and the 
#program will tell the user if the number is even or odd

even_number = input('Please enter an even number: ')

if int(even_number) % 2 == 0:
    print('You have entered an even number')

else:
    print('You have entered an odd number')

