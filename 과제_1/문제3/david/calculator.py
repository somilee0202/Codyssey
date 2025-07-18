def cal():
    try:
        a = float(input("Input number1: "))
        b = float(input("Input number2: "))
    except ValueError:
        print("Invalid number input.")
        return
    
    operator = input("Input Operator: ")

    if operator == "+":
        print(a + b)
    elif operator == "-":
        print(a - b)
    elif operator == "*":
        print(a * b)
    elif operator == "/":
        if b == 0:
            print("Error: Division by zero.")
        else:
            print(a / b)

    else:
        print("Invalid operator." )

if __name__ == "__main__":
    cal()