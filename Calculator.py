def Add(value1 , value2):
    return value1 + value2

def Sub(value1 , value2):
    return value1 - value2

def Mul(value1 , value2):
    return value1 * value2
def Div(value1 , value2):
    if value2 == 0:
        print('Invalid')
    else:
        return value1/value2


value1 = int(input('Enter value1: '))
operator = input('operator (+,-,*,/): ')
value2 = int(input('Enter value2: '))

if operator == '+':
    print(Add(value1 , value2))
elif operator == '-':
    print(Sub(value1 , value2))
elif operator == '*':
    print(Mul(value2 , value2))
else:
    print(Div(value1 , value2))