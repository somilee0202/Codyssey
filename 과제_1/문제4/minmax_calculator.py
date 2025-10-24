def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return arr

def main():
    try:
        arr = list(map(float, input("숫자들을 입력하세요: ").split()))
        if not arr: # arr이 비어있다면
            print("Invalid Input.")
            return
    except:
        print("Invalid Input")
        return

    arr = sort(arr)
    print(f"Min: {arr[0]}, Max: {arr[-1]}")  # arr[-1] → 마지막 원소

if __name__ == "__main__":
    main()