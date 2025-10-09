def binary_search(arr, target):
    sorted_arr = sorted(arr)
    left, right = 0, len(sorted_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] == target:
            return mid, sorted_arr
        elif sorted_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, sorted_arr


try:
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
    target = int(input("Введите число для поиска: "))
    
    result, sorted_numbers = binary_search(numbers, target)
    
    print(f"Отсортированный список: {sorted_numbers}")
    
    if result != -1:
        print(f"Число {target} найдено на позиции {result} в отсортированном списке")
    else:
        print(f"Число {target} не найдено")
        
except ValueError:
    print("Ошибка! Убедитесь, что вводите только целые числа.")
