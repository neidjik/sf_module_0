version2

def game_core_v3(number):
    import numpy as np
    number=0
    count=0 # zero count
    n1=1 #begin of range
    n2=101 # end of range
    predict = np.random.randint(1,100) # made a number
    while number != predict:
        number=(n1+n2) // 2 # count middle of range
        count+=1
        if number>predict:
            n2=number # change range
        else:
            n1=number # change range
    return(count)
 
score_game(game_core_v3)