#Problem 1

try:
    num1=float(input('Enter the first number: '))
    op=input('Enter the operation(+, -, *, /): ')
    num2=float(input('Enter the second number: '))

#compute directly in each branch
    if op=='+':
        print(f'result is {num1+num2}')
    elif op=='-':
        print(f'result is {num1-num2}')
    elif op=='*':
        print(f'result is {num1*num2}')
    elif op=='/':
        print(f'result is {num1/num2}')
    else:
        print('Error: Invalid operator')

except ZeroDivisionError:
    print('you cannot divide by zero :(')
except ValueError:
    print('Please enter a valid number!')

#Problem 2

#repitition
try:
    salest=float(input('Enter sales target: '))
    cusales=0.0
    for days in range(1,6):
        dsales=float(input(f'Enter day {days} sales: '))
        cusales+=dsales
        if salest>0:
            percentage=(cusales/salest)*100
        else:
            percentage=0.0
        print(f'cumulative sales: {cusales:.1f} ({percentage:.1f}%)')
except ValueError:
    print('Please enter a valid number!')






