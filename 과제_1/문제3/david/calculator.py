def add(a, b):
    print(f"Result: <{a + b}>")
    return

def sub(a, b):
    print(f"Result: <{a - b}>")
    return

def mul(a, b):
    print(f"Result: <{a * b}>")
    return

def div(a, b):
    if b == 0:
        print("Error: Division by zero.")
    else:
        print(f"Result: <{a / b}>")
    return

def cal():
    try:
        a = int(input("Enter number1: "))
        b = int(input("Enter number2: "))
    except ValueError:
        print("Invalid number input.")
        return
    
    operator = input("Enter Operator: ")

    if operator == "+":
        add(a, b)
    elif operator == "-":
        sub(a, b)
    elif operator == "*":
        mul(a, b)
    elif operator == "/":
        div(a, b)

    else:
        print("Invalid operator." )

if __name__ == "__main__":
    cal()