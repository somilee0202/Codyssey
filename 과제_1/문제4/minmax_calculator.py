def sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap
    return arr

def main():
    arr = list(map(float, input("숫자들을 입력하세요: ").split()))
    if len(arr) == 0:
        print("Enter numbers")
        return
    sort(arr)
    print(f"min = {arr[0]}, max = {arr[-1]}")  # arr[-1] → 마지막 원소

if __name__ == "__main__":
    main()