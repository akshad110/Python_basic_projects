import os

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "invalid number."
    else:
        return a/b


operation={
    "+":add,
    "-":sub,
    "*":mul,
    "/":div
}

def calculator():
    num1 = float(input("Enter the number one: "))
    for symbol in operation:
        print(symbol)
    flag = True
    while flag:
        op_symbol = input("Pick an operator: ")
        num2 = float(input("Enter the number two: "))
        calculator_function = operation[op_symbol]
        output = calculator_function(num1, num2)
        print(f"{num1} {op_symbol} {num2} = {output}")

        should_cont = input(
            f"Enter 'y' to continue calculation with {output} or 'n' to start with new calculation or 'x' to  exit: ").lower()
        if should_cont == 'y':
            num1 = output
        elif should_cont == 'n':
            flag = False
            os.system('cls')
            calculator()
        else:
            flag = False
            print("Bye.")


calculator()





