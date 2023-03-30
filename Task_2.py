"""
Задача 28: Напишите рекурсивную функцию
sum(a, b), возвращающую сумму двух целых
неотрицательных чисел. Из всех арифметических
операций допускаются только +1 и -1.
Также нельзя использовать циклы.

2 2
4
"""
def user_input(message, min_elem, max_elem):
    input_error: bool = True
    while input_error:
        try:
            number = int(input(message))
        except:
            print("Вы ввели не число!")
        else:
            if min_elem < number:
                input_error = False
            else:
                print("Вы ввели число, не соответствующее условию!")
    return number

def sum_function(num1: int, num2: int):
    if num2 == 1:
        return num1 + 1
    return sum_function(num1, num2 - 1) + 1

num_a = user_input(message = "Введите первое целое положительное число: ", min_elem = 0, max_elem = 0)
num_b = user_input(message = "Введите второе целое положительное число: ", min_elem = 0, max_elem = 0)

print(sum_function(num_a, num_b))

