def do_cowscheck(secret_number, guess):
    cows=0
    for i in range(4):
        if guess[i] in secret_number:
            cows+=1
    return cows
