import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функция выполнялась {end - start:.10f} секунд")
        return result
    return wrapper

@timer
def test_func1():
    summ = 0
    for i in range(1,1001):
        summ += i
    return summ

@timer
def test_func2(n):
    summ = 0
    for i in range(1,n):
        summ += 1000000*i
    return summ


result1 = test_func1()
print(f"Сумма чисел от 1 до 1000: {result1}")

result2 = test_func2(n=1001)
print(f"Сумма 1000000*i от 1 до n: {result2}")
