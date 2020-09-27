def squares(a, b):
    
    #math.sqrt - find the root square number and floor for for both a-1 and b
    #use a-1 to get a included example: a=1, b=2 countPerfectSquares = 1 - 0
    #substract both values to count the number of perfect squares between a and b
    b = math.floor(math.sqrt(b))
    a = math.floor(math.sqrt(a-1))
    countPerfectSquares = b - a
    return countPerfectSquares