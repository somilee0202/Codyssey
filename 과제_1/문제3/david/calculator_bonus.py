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
        a, operator, b = input("Enter expression: ").split(" ")
    except ValueError as e:
        print(f"Error: {e}")
        return

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number input.")
        return

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