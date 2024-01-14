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
