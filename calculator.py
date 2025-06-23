def addition():
    input_1 = float(input("Enter the First value: "))
    input_2 = float(input("Enter the Second value: "))
    print("The Sum of the two values is:", input_1 + input_2)

def subtraction():
    input_1 = float(input("Enter the First value: "))
    input_2 = float(input("Enter the Second value: "))
    print("The Difference of the two values is:", input_1 - input_2)

def multiplication():
    input_1 = float(input("Enter the First value: "))
    input_2 = float(input("Enter the Second value: "))
    print("The Product of the two values is:", input_1 * input_2)

def division():
    input_1 = float(input("Enter the First value: "))
    input_2 = float(input("Enter the Second value: "))
    if input_2 != 0:
        print("The Quotient of the two values is:", input_1 / input_2)
    else:
        print("Division by zero is not allowed.")

def modulo():
    input_1 = float(input("Enter the First value: "))
    input_2 = float(input("Enter the Second value: "))
    if input_2 != 0:
        print("The Remainder of the values is:", input_1 % input_2)
    else:
        print("Modulo by zero is not allowed.")

while True:
    x = input(
    '''
Choose an operation:
   for Addition type:+
    for Subtraction type:-
    for Multiplication type:*
    for Division type:/
    for Modulo type:%            
    to quit type:0   
Enter a symbol for desired operation: ''')

    if x == '+':
        addition()
    elif x == '-':
        subtraction()
    elif x == '*':
        multiplication()
    elif x == '/':
        division()
    elif x == '%':
        modulo()
    elif x == '0':
        print("Quitting the process...")
        break
else:
        print("Enter a valid symbol.")
