

grade_mark = input('Please enter the grade you would like to check: ')

if float(grade_mark) < 40:
    print('Fail')

elif float(grade_mark) < 50:
    print('Pass')

elif float(grade_mark) < 60:
    print('Merit 2')

elif float(grade_mark) < 70:
    print('Merit 1')

else:
    print('Distinction')


