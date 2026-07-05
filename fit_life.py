# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30  # мл воды на 1 кг веса
ML_IN_LITER = 1000  # количество мл в литре


def fitlife_bot():
    """Главная функция бота"""
    # Мне проще создать одну функцию, чем множество и возвращать результат
    # 1. Знакомство
    user_name = input('Добро пожаловать! Как вас зовут?')
    user_age = int(input('Какой ваш возарст?'))

    # 2. Сбор данных

    user_weight = float(input('Введите ваш вес (в кг)'))
    user_height = float(input('Введите ваш рост (в метрах, например 1.75)'))

    # Расчет ИМТ:
    bmi = round(user_weight / (user_height**2), 1)

    # Подсчет воды:
    water_ml = user_weight * WATER_PER_KG
    water_needed_l = round((water_ml / ML_IN_LITER), 2)

    # 4. Вывод красивого результата
    print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
    print(f"Твой Индекс Массы Тела: {bmi}")
    print(f"Рекомендуемая норма воды: {water_needed_l} л. в день")

    print("Расчет окончен. Будьте здоровы!")


fitlife_bot()
