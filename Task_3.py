"""
Дана последовательность натуральных чисел
(одно число в строке), завершающаяся числом 0.
Определите значение второго по величине элемента
в этой последовательности, то есть элемента,
который будет наибольшим, если из последовательности
удалить наибольший элемент. В этой задаче нельзя
использовать глобальные переменные. Функция получает
данные, считывая их с клавиатуры, а не получая их в
виде параметра. В программе на языке Python функция
возвращает результат в виде кортежа из нескольких
чисел и функция вообще не получает никаких параметров.
Других параметров, кроме как используемых для возврата
значения, функция не получает.
Гарантируется, что последовательность содержит хотя
бы два числа (кроме нуля).

1 3 5 7 3 6 8 4 3 2 0 -> 7

1 2 3 4 5 6 3 1 2 5 3 -> 5
"""

def find_second_max():
    list_user = []
    end_input: bool = 1
    while end_input != 0:
        user_num = int(input('Введите натуральное число (закончить ввод -> 0)'))
        if user_num == 0:
            end_input = 0
        else:
            list_user.append(user_num)
    if list_user[0] > list_user[1]:
        first_max = list_user[0]
        second_max = list_user[1]
    else:
        first_max = list_user[1]
        second_max = list_user[0]
    for i in range(2, len(list_user)):
        if list_user[i] > first_max:
            second_max = first_max
            first_max = list_user[i]
        elif second_max < list_user[i] < first_max:
            second_max = list_user[i]
    res_str = f'В последовательности {list_user} второй по величене элемент равен {second_max}.'
    return res_str


print(find_second_max())


