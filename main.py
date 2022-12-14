from math import sin
from math import cos
from math import tan

def trigFuction(a, x):
    a = makeValue(str(a))
    x = str(x)
    match x:
        case 'sin':
           stack.append(sin(a)) 
        case 'cos':
            stack.append(cos(a))   
        case 'tan':
            stack.append(tan(a))

def calculate(a, b, x):
   
    a = makeValue(str(a))
    b = makeValue(str(b))
    
    match x:
        case '+':
            stack.append(a+b)
        case '-':
            stack.append(a-b)
        case '*':
            stack.append(a*b)
        case '/':
            stack.append(a/b)

def makeValue(x):
    if'.' in x:
        return float(x)
    else:
        return int(x)

def solve(equation):
    for x in equation:
        if x in trig:
            a = stack.pop()
            trigFuction(a,x)
        elif x in operations:
            b = stack.pop()
            a = stack.pop()
            calculate(a, b, x)
        else:
            stack.append(x)
    return stack.pop()


def prepEquation(equation = ''):
    parenMult = equation.count(") (")
    equation = equation.split(" ")
    for x in range(parenMult):
        equation.append('*')
    try:
        while True:
            equation.remove("(")
            equation.remove(")")
    except ValueError:
        pass
    return equation
    
def help():
    equations = []
    equations.append("1 2 +")
    equations.append("2 ( 2 sin ) *")
    equations.append("2 ( 2.5 1 + ) ( 2 3 + ) +")

    exampleNumber = 1
    for equation in equations:
        print(f"Example Number {exampleNumber}:\n Reverse Polish Notation: {equation}")
        equation = prepEquation(equation)
        print(f"Result: {solve(equation)}\n")
        exampleNumber += 1
    equation = input('Enter your equation (space between each value): ')
    return equation

trig = ['sin', 'cos','tan']
operations = ['+', '-', '*', '/']
stack = []

equation = input('Enter your equation (space between each value) or Enter \'help\' for examples\n')
if equation == 'help':
    print(solve(prepEquation(help())))
else:
    print(solve(prepEquation(equation)))










