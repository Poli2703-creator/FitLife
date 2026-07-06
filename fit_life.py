# Проект FitLife - MVP версия 2.0

WATER_PER_KG = 30  # мл воды на 1 кг веса
ML_IN_LITER = 1000  # количество мл в литре


def main():
    """Главная функция бота FitLife."""
    # если я ставлю двойные, то текст перестает выделяться

    # 1. Знакомство
    user_name = input('Добро пожаловать! Как вас зовут? ')

    # ввод возраста с циклом и защитой от ошибок
    while True:
        try:
            user_age = int(input('Какой ваш возраст? (введите число): '))
            break
        except ValueError:
            print('Ошибка! Нужно ввести целое число (например, 25).')

    # 2. Сбор данных (добавила пробелы перед вводом данных для красоты)
    # ввод веса с циклом и защитой от ошибок
    while True:
        try:
            user_weight = float(input('Введите ваш вес: ').replace(',', '.'))
            break
        except ValueError:  # если вводит не число
            print('Ошибка! Нужно ввести число в кг (например, 70.5).')

    # ввод роста с циклом и защитой от ошибок
    while True:
        try:
            user_height = float(input('Введите ваш рост: ').replace(',', '.'))
            break
        except ValueError:  # если вводит не число
            print('Ошибка! Нужно ввести число в метрах (например, 1.75).')

    # Расчет ИМТ:
    bmi = round(user_weight / (user_height ** 2), 1)

    # Подсчет воды:
    water_ml = user_weight * WATER_PER_KG
    water_needed_l = round((water_ml / ML_IN_LITER), 2)

    # Возвращаю все вычисленные значения
    return user_name, user_age, bmi, water_needed_l


if __name__ == '__main__':
    user_name, user_age, bmi, water_needed_l = main()

    # Результат одним print() и звменила кавычки
    print(
        f'Отчет для пользователя: {user_name} ({user_age} г.)\n'
        f'Твой Индекс Массы Тела: {bmi}\n'
        f'Рекомендуемая норма воды: {water_needed_l} л. в день\n'
        'Расчет окончен. Будьте здоровы!',
    )
