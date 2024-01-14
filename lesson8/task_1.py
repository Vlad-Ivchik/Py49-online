
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
