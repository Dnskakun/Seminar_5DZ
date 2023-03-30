"""
Задача 26: Напишите программу, которая на
вход принимает два числа A и B, и возводит
число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
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

def degree_function(num1: int, num2: int, res: int = 1):
    if num2 == 1:
        return res * num1
    return num1 * degree_function(num1, num2 - 1, res)


num_base = user_input(message = "Введите целое положительное число, которое будем возводить в степень: ", min_elem = 0, max_elem = 0)
num_degree = user_input(message = "Введите целое положительное число (показатель степени): ", min_elem = 0, max_elem = 0)

print(degree_function(num_base, num_degree))



