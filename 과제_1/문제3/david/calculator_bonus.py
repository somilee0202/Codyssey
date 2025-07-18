def cal():
    try:
        a, operator, b = input("Enter expression: ").split(" ")
        print(f"a= {a}, operator= {operator}, b= {b}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    cal()