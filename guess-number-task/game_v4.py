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
        predict_number = np.random.randint(1, 101)  # предполагаемое число от 1 по 100 включительно
        if number == predict_number:
            break  # выход из цикла если угадали c первого рандомного числа

        if predict_number < number: # Если рандомное число меньше загаданного
            
            if number < 50:
                
                if number > 25:
                    
                    predict_number = np.random.randint(26, 50)
                    if number == predict_number:
                        break  # выход из цикла если угадали                
                
                elif number < 26:
                    
                    if number < 13:
                        
                        predict_number = np.random.randint(1, 13)
                        if number == predict_number:
                            break  # выход из цикла если угадали
                       
                        if number > 7:
                        
                            predict_number = np.random.randint(7, 13)
                            if number == predict_number:
                                break  # выход из цикла если угадал
                                      
                    if number > 18:    
                        
                        predict_number = np.random.randint(19, 26)
                        if number == predict_number:
                            break  # выход из цикла если угадали
                                            
                    if number > 12:
                        
                        predict_number = np.random.randint(13, 26)
                        if number == predict_number:
                            break  # выход из цикла если угадал
                        
                    if number > 7:
                        
                        predict_number = np.random.randint(7, 13)
                        if number == predict_number:
                            break  # выход из цикла если угадал
                    
                if number > 25:
                    
                    predict_number = np.random.randint(26, 50)
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
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

#res_list = []
#for i in range(1, 100):
#    score = score_game(random_predict)
#    res_list.append(score)
#print(max(res_list))

if __name__ == "__main__":
    # RUN
    score_game(random_predict)