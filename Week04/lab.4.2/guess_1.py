
number_to_guess = 32

guess = int(input('Please guess the number: '))
while guess != number_to_guess:
    print('Wrong!')
    guess = int(input('Please guess again: '))

print('You have correctly guessed:', number_to_guess)



