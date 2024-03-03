#I am writing an application, at the moment, in it I take an input of an amount 
#in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a 
#minus sign, and the bank takes in the amount in cent, (944). Write a program 
#called convert.py that takes in a float amount of dollars and returns that 
#absolute amount in cent.

#Please enter an amount:-5.99 
#That amount in cent is :599

balance = float(input('Enter your bank account balance: €'))
converted_balance = abs(balance) * 100
print('Your absolute balance is {} cent'.format(converted_balance))

