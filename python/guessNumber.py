def guess(number):
    if number > 2:
        return -1
    elif number < 2:
        return 1
    else:
        return 0
def guessNumber(n):
    if n == 1:
        return 1
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
            if top == currentGuess:
                currentGuess -= 1
        else:
            bottom = currentGuess
            currentGuess = (top+bottom)//2
            if bottom == currentGuess:
                currentGuess += 1



print(guessNumber(2))