import numpy as np

def score_game(game_core_v1):
    '''«апускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"¬аш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

def game_core_v3(number):
    count=0 # zero count
    n1=1 #begin of range
    n2=101 # end of range
    predict=0
    while number != predict:
        predict=(n1+n2) // 2 # count middle of range
        count+=1
        if predict>number:
            n2=predict # change range
        else:
            n1=predict # change range
    return(count)

score_game(game_core_v3)