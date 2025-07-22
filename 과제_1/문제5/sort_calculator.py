def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    try:
        arr = list(map(float, input("Enter numbers: ").split()))
        if not arr:
            print("Invalid input.")
            return
    except:
        print("Invalid input.")
        return

    bubble_sort(arr)
    sorted = ' '.join(f"<{num}>" for num in arr)
    print(f"Sorted: {sorted}") 

if __name__ == "__main__":
    main()