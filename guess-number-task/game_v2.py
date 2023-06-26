"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


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
            break  # выход из цикла если угадали с первого раза
        
        if predict_number < number: # Если рандомное число меньше загаданного
            diff_betw = number - predict_number # Разница между рандомным и загаданным числами            
            predict_number += diff_betw # Рандомное число это сумма Рандомного числа и разницы
            if number == predict_number:
                break  # выход из цикла если угадали
            
        if predict_number > number: # Если рандомное число больше загаданного            
            diff_betw = predict_number - number # Разница между рандомным и загаданным числами            
            predict_number -= diff_betw # Рандомное число это разница Рандомного числа и diff_betw            
            if number == predict_number:
                break  # выход из цикла если угадали
            
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
