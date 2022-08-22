def add(num1, num2):
    result = num1 + num2
    print(result , "\n")

#add(number1, number2)

def subtract(num1, num2):
    result = num1 - num2
    print(result , "\n")

#subtract(number1, number2)

def multiply(num1, num2):
    result = num1 * num2
    print(result , "\n")

#multiply(number1, number2)

def divide(num1, num2):
    result = num1 / num2
    print(result , "\n")

#divide(number1, number2)

def mod(num1, num2):
    result = num1 % num2
    print(result , "\n")



def exp(num1, num2):
    result = num1 ** num2
    print(result , "\n")

x = True

while x:
    print(" 1:Add \n 2:Subtract \n 3:Multiply \n 4:Divide \n 5:Mod \n 6:Exponentiate \n")

    selection = int(input("Selection: "))

    number1 = int(input("First Number: "))
    number2 = int(input("Second Number: "))

    if selection == 1:
        add(number1, number2)
    elif selection == 2:
        subtract(number1, number2)
    elif selection == 3:
        multiply(number1, number2)
    elif selection == 4:
        divide(number1, number2)
    elif selection == 5:
        mod(number1, number2)
    elif selection == 6:
        exp(number1, number2)
    else:
        x = False