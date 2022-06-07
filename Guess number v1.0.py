import random


def number():
    ans = random.randint(0, 101)
    return ans

def choose():
    choose = str(input("Choose a difficulty. 'easy' or 'hard': "))
    if choose == "easy":
        print("You have 10 attemps")
        attemps = 10
    elif choose == "hard":
        print("You have 5 attemps")
        attemps = 5
    
    return attemps 

def start():
    ans = number()
    attemos = choose()
    GG = False
    while not GG == True:
        Guess = int(input("Guess a number: "))
        if ans > Guess:
            print("too low.")
            attemos -= 1
            print(f"You have {attemos} remaining to guess the number.")
        elif ans == Guess:
            print(f"You got it! The answer is {ans}")
            GG = True 
        elif ans < Guess:
            print("too high.")
            attemos -= 1
            print(f"You have {attemos} remaining to guess the number.")
        if attemos == 0:
            print("You have run out of guesses, you lose.")
            print(f"The answer is {ans}.")
            GG = True


END = "Y"
while not END == "N":
    start()
    END = str(input("Do you want to play again? (Y / N)"))
    
        
        

    


