def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def cal_muldiv(arr):
    result = []
    i = 0
    while i < len(arr):
        if arr[i] == '*':
            a = result.pop()
            b = arr[i + 1]
            result.append(mul(a, b))
            i += 2
        elif arr[i] == '/':
            a = result.pop()
            b = arr[i + 1]
            result.append(div(a, b))
            i += 2
        else:
            result.append(arr[i])
            i += 1
    return result

def cal_addsub(arr):
    result = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] == '+':
            result = result + arr[i + 1]
            i += 2
        elif arr[i] == '-':
            result = result - arr[i + 1]
            i += 2
    return result


def check_possible(arr):
    for i in range(len(arr)):
        if i%2 == 0:
            try:
                arr[i] = float(arr[i])
            except:
                print("Invalid input.")
                return
        else:
            if arr[i] not in "+-*/":
                print("Invalid input.")
                return
            
    return arr

def cal(arr):
    arr = check_possible(arr)
    if arr is None:
        return
    try:
        arr = cal_muldiv(arr)
        result = cal_addsub(arr)
        return result
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except:
        print("Invalid input")

def main():
    arr = list(input("Enter expression: ").split())
    if len(arr)%2 == 0:
        print("Invalid input.")
        return    
    result = cal(arr)
    if result is not None:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()