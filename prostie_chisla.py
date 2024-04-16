def is_prime(n):
    """Проверяет, является ли число простым"""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(minimum, maximum):
    """Возвращает список всех простых чисел в заданном диапазоне"""
    primes = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Получаем от пользователя минимальное и максимальное значения
min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))

# Находим простые числа в заданном диапазоне и выводим результат
print(f"Простые числа в диапазоне от {min_val} до {max_val}:")
print(find_primes(min_val, max_val))
