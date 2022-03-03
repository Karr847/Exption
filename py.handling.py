#exception= event detected during execution that interupt the flow of a program
try:
    numerator=int(input('Enter a number to divide :'))
    denominator=int(input('Enter a number to divide by :'))
    result= numerator/ denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print('you cannot divide by zero: idiot!')
except ValueError as e:

    print(e)
    print('enter only number plz')
except Exception as e:
    print(e)
    print('something went wrong:(')
else:
    print(result)
finally:
    print('This will always execute')
