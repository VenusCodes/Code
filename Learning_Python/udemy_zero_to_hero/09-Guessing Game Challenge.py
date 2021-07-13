from random import randint
target = randint(1,100)
print(target)
print("welcome  to the guess")
guesses = []
while True:
    guess = int(input("Guess > "))

    if guess < 1 or guess > 100:
        print('OUT OF BOUND! plzz select between 0 and 100:')
        continue
    
    if guess == target:
        print(f'Congrats, you gueessed it in only {len(guesses)} GUESSES!')
        break
    
    guesses.append(guess)
    
    if guesses[-1]:  
        if abs(target-guess) < abs(target-guesses[-1]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(target-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
    pass
