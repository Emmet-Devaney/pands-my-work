import random

number_to_guess = random.randint (1,100)

guess = int(input('Please guess the number from 1 - 100: '))

while guess != number_to_guess:
    if guess < number_to_guess:
        print('Too low')
        guess = int(input('Please guess the number: '))
    
    elif guess > number_to_guess:
        print('Too High')
        guess = int(input('Please guess the number: '))
    
print('You have correctly guessed:', number_to_guess)

