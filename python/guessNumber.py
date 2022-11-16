def guess(number):
    if number > 6:
        return -1
    elif number < 6:
        return 1
    else:
        return 0
def guessNumber(n):
    currentGuess = n//2
    bottom = 1
    top = n
    while top <= n and bottom > 0:
        var = guess(currentGuess)
        if var == 0:
            return currentGuess
        elif var == -1:
            top = currentGuess
            currentGuess = (top+bottom)//2
        else:
            bottom = currentGuess
            currentGuess = (top+bottom)//2



print(guessNumber(10))