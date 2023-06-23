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
            break  # выход из цикла если угадали c первого рандомного числа
        
        if predict_number < number < 50: #######################################################   М50

            if predict_number < number < 26:
                if number == predict_number:
                    break  # выход из цикла если угадали
                if predict_number < number < 13:                           # ММ12
                    predict_number = np.random.randint(1, 13)
                    if number == predict_number:
                        break  # выход из цикла если угадали
                    if predict_number < number < 7:
                        predict_number = np.random.randint(1, 7)
                        if number == predict_number:
                            break  # выход из цикла если угадали
                  
                if predict_number < number > 18:
                        predict_number = np.random.randint(19, 26)                        
                        if number == predict_number:
                            break  # выход из цикла если угадали
                        
                elif predict_number < number > 12:                           # МБ12
                    predict_number = np.random.randint(13, 26)
                    if number == predict_number:
                        break  # выход из цикла если угадали

            if predict_number < number > 25:
                predict_number = np.random.randint(26, 50)
                if number == predict_number:
                    break  # выход из цикла если угадали
                   
                if predict_number < number > 37:                           # МБ37
                    predict_number = np.random.randint(38, 50)
                    if number == predict_number:
                       break  # выход из цикла если угадали

                elif predict_number < number < 37:                           # ММ37
                    predict_number = np.random.randint(26, 37)
                    if number == predict_number:
                       break  # выход из цикла если угадали
                                     
            if predict_number > number > 25:
                    predict_number = np.random.randint(26, 50)
                    if number == predict_number:
                       break  # выход из цикла если угадали
            
                    if predict_number > number > 37:
                       predict_number = np.random.randint(38, 50)
                       if number == predict_number:
                           break  # выход из цикла если угадали
                
            if predict_number < number < 37:
                predict_number = np.random.randint(26, 37)
                if number == predict_number:
                    break  # выход из цикла если угадали
                   
            if predict_number > number < 37:
                predict_number = np.random.randint(26, 37)
                if number == predict_number:
                    break  # выход из цикла если угадали
        elif predict_number > number < 51:#######################################################   М50
            
            if predict_number > number < 25:
                predict_number = np.random.randint(1, 25)
                if number == predict_number:
                    break  # выход из цикла если угадали

            if predict_number > number > 25:
                predict_number = np.random.randint(26, 51)
                if number == predict_number:
                    break  # выход из цикла если угадали
                
        elif predict_number > number > 49:########################################################   Б50
            
            predict_number = np.random.randint(50, 101)
            if number == predict_number:
                break  # выход из цикла если угадали
            
            if predict_number > number > 75:
                predict_number = np.random.randint(76, 101)
                if number == predict_number:
                    break  # выход из цикла если угадали
                
            if predict_number > number < 75:
                predict_number = np.random.randint(50, 75)
                if number == predict_number:
                    break  # выход из цикла если угадали

        elif predict_number < number > 50:#########################################################   Б50
            
            predict_number = np.random.randint(51, 101)
            if number == predict_number:
                break  # выход из цикла если угадали
            
            if predict_number > number > 50:
                predict_number = np.random.randint(51, 101)
                if number == predict_number:
                    break  # выход из цикла если угадали
                
            if predict_number < number < 76:
                predict_number = np.random.randint(50, 76)
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
    np.random.seed(85)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)