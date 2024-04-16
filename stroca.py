def sort_by_length(strings):
    """Сортировка списка строк по длине"""
    # Сначала сортируем по возрастанию длины
    sorted_strings = sorted(strings, key=len)
    # Затем сортируем по убыванию длины, используя обратный порядок
    sorted_strings_reverse = sorted(strings, key=len, reverse=True)
    return sorted_strings, sorted_strings_reverse

# Получаем от пользователя список строк
strings = input("Введите список строк через запятую: ").split(",")

# Убираем лишние пробелы вокруг строк
strings = [s.strip() for s in strings]

# Применяем функцию сортировки к введенному списку
sorted_asc, sorted_desc = sort_by_length(strings)

# Выводим отсортированные списки
print("Список строк, отсортированный по длине (по возрастанию):")
print(sorted_asc)

print("\nСписок строк, отсортированный по длине (по убыванию):")
print(sorted_desc)
