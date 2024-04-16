def unique_elements():
    input_str = input("Введите числа через пробел для проверки уникальности: ")
    input_list = list(map(int, input_str.split()))
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list

print(unique_elements())

