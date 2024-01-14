'''Тема: Работа с исключениями'''

'''1. Реализовать программу для подсчёта индекса массы тела
человека. Пользователь вводит рост и вес с клавиатуры.
TeachMeSkills.by
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать
обработку исключений.'''


def imt():
    try:
        weight = float(input('Введите свой вес, кг. '))
        height = float(input('Введите свой рост, см. '))
        sum_imt = weight / (height / 100) ** 2

        print(f'Ваш ИМТ равен {sum_imt:.2f}')

        if weight == 0 or sum_imt == 0:
            raise ValueError('Нельзя вводить нулевой вес')
        elif sum_imt <= 18.5:
            print('Недостаточный вес')
        elif sum_imt <= 24.9:
            print('Обычный вес')
        elif sum_imt <= 29.9:
            print('Избыточный вес')
        elif sum_imt > 30:
            print('Ожирение')
    except ZeroDivisionError as e:
        print(f'Ошибка деления на ноль: {e}')
    except ValueError as e:
        print(f'Ошибка ввода данных: {e}')
    except Exception as e:
        print(f'Другая ошибка: {e}')


imt()


'''2. Реализовать программу с функционалом калькулятора
для операций над двумя числами. Числа и операция
вводятся пользователем с клавиатуры. Использовать
ООП. Использовать обработку исключений.'''


def calc():
    try:
        first_number = float(input('Введите первое число '))
        operator = input('Введите оператор ')
        second_number = float(input('Введите второе число '))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            result = first_number / second_number
        else:
            print("Ошибка: неверный оператор!")
            exit()
        print(f"Результат равен:, {result}")

    except ZeroDivisionError as e:
        print(f'Ошибка деления на ноль: {e}')

    except ValueError as e:
        print(f'Ошибка ввода данных: {e}')

    except Exception as e:
        print(f'Другая ошибка: {e}')


calc()
