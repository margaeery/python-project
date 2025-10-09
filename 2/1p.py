def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


try:
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
    print("Отсортированный список:", bubble_sort(numbers))
except ValueError:
    print("Ошибка! Убедитесь, что вводите только целые числа.")
