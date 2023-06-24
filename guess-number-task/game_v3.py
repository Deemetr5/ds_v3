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

        if predict_number < number < 50: #######################################################   М50    predict_number <  <50  !!!!!!!!!!!!!
            if predict_number < number < 26:                                                               #<26  <50 
                
                if predict_number < number < 13:                           # ММ12                          # < 13  < 50 
                    predict_number = np.random.randint(1, 13)
                    if number == predict_number:
                        break  # выход из цикла если угадали
                    
                    if predict_number < number < 7:                                                       # < 7  < 50 
                        predict_number = np.random.randint(1, 7)
                        if number == predict_number:
                            break  # выход из цикла если угадали

                if predict_number < number > 18:                                                         # > 18  < 50 
                        predict_number = np.random.randint(19, 26)                        
                        if number == predict_number:
                            break  # выход из цикла если угадали

                elif predict_number < number > 12:                           # МБ12                      # > 12  < 50 
                    predict_number = np.random.randint(13, 26)
                    if number == predict_number:
                        break  # выход из цикла если угадали

            if predict_number < number > 25:                                                             # > 25  < 50 
                predict_number = np.random.randint(26, 50)
                if number == predict_number:
                    break  # выход из цикла если угадали

                if predict_number < number > 37:                           # МБ37                        # > 25 > 37 < 50 
                    predict_number = np.random.randint(38, 50)
                    if number == predict_number:
                       break  # выход из цикла если угадали

                elif predict_number < number < 37:                           # ММ37                       # > 25 < 37 < 50 
                    predict_number = np.random.randint(26, 37)
                    if number == predict_number:
                       break  # выход из цикла если угадали
                   
                                      

            if predict_number > number > 25:                                                           # > 25 < 50 
                predict_number = np.random.randint(26, 50)
                if number == predict_number:
                    break  # выход из цикла если угадали

                if predict_number > number > 37:                                                     # > 25 > 37 < 50 
                    predict_number = np.random.randint(38, 50)
                    if number == predict_number:
                        break  # выход из цикла если угадали

            if predict_number < number < 37:                                                          # < 37 < 50 
                predict_number = np.random.randint(26, 37)
                if number == predict_number:
                    break  # выход из цикла если угадали
              
        elif predict_number > number < 51:#######################################################   predict_number >    < 51 
            
            if predict_number > number < 25:                                                             # < 25 < 51 
                predict_number = np.random.randint(1, 25)
                if number == predict_number:
                    break  # выход из цикла если угадали

            if predict_number > number > 25:                                                            # > 25 < 51 
                predict_number = np.random.randint(26, 51)
                if number == predict_number:
                    break  # выход из цикла если угадали
                
        elif predict_number > number > 49: ########################################################     # predict_number >  > 49 
            
            predict_number = np.random.randint(50, 101)
            if number == predict_number:
                break  # выход из цикла если угадали
            
            if predict_number > number > 75:                                                        # > 49 > 75
                predict_number = np.random.randint(76, 101)
                if number == predict_number:
                    break  # выход из цикла если угадали
                
            if predict_number > number < 75:                                                        # > 49 < 75
                predict_number = np.random.randint(50, 75)
                if number == predict_number:
                    break  # выход из цикла если угадали

        elif predict_number < number > 50: #########################################################  predict_number < > 50

            predict_number = np.random.randint(51, 101)
            if number == predict_number:
                break  # выход из цикла если угадали    
              
            if predict_number > number > 50:                                                 #  > 50
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
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    #print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

res_list = []
for i in range(1, 100):
    score = score_game(random_predict)
    res_list.append(score)
print(max(res_list))

if __name__ == "__main__":
    # RUN
    score_game(random_predict)