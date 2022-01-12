"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binary_finder(number: int = 1) -> int:
    """Находим число через бинарный поиск

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count, limit_lower, limit_upper = 0, 0, 101

    predict = np.random.randint(limit_lower, limit_upper)

    while number != predict:
        count += 1

        if number > predict:
            limit_lower = predict
            predict = round(limit_upper - (limit_upper - limit_lower) / 2)

        elif number < predict:
            limit_upper = predict
            predict = round(limit_upper - (limit_upper - limit_lower) / 2)

    return count


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binary_finder)