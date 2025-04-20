# Computer will select a random number between 1 and 50 (inclusive).
# Computer will then accept player guess, and evaluate based on the following:
    # if guess is higher than the chosen number, player will be informed to guess again.
    # if guess is lower than the chosen number, player will be informed to guess again.
# if guess matches the chosen number, the correct answer will end the game.
    
sentence1 = "Guess a number from 1-50, a correct answer will win the game."

print()
print(sentence1)


import random
num = random.randint(1, 50)
print()
playerguess = int(input("Guess a number from 1 to 50:"))
print()
while playerguess != num:
    if playerguess > num:
        print()
        print("Your guess is higher than the chosen number!")
        playerguess = int(input("Guess again:"))  
    elif playerguess < num:
        print()
        print("Your guess is lower than the chosen number!")
        playerguess = int(input("Guess again:"))
    else:
        break
    print()
print("You guessed correctly!! End of game")
print("Author-Christina James, Dec '24")
    
    
