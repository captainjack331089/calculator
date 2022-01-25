from art import logo
from  replit import clear
def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+": add,
    "-": minus,
    "*": multiply,
    "/": divide,
}
def  calculator():
    print(logo)
    status= 1
    first_num = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    while status:
        operation = input("Pick an Operation: ")
        second_num = float(input("What's the next number?: "))
        print(type(operations[operation]))
        result = operations[operation](first_num,second_num)
        print(f"{first_num} {operation} {second_num} = {result}")

        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'c' to start a new calculation or Type 'n' to exit.:")
        if should_continue == 'y':
            first_num = result
        elif should_continue == 'c':
            status = 0
            clear()
            calculator()
        elif should_continue == 'n':
            status = 0
            clear()


calculator()