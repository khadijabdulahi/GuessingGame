import random 
greeting = input('Howdy, what\'s your name?')
print(f'{greeting}, I\m thinking of a number between 1 and 100.')
print('Try to guess my number')
best_score = 100000
def guessing_game():
    global best_score
    print(best_score)
    comp_number = random.randrange(1, 10)
    guess = int(input('Your guess? '))
    count = 1
    while guess != comp_number:
        if guess < comp_number:
            print("Your guess is too low, try again.")
            guess = int(input('Your guess? '))
        else: 
            print("Your guess is too high, try again.")
            guess = int(input('Your guess? '))
        count = count + 1 
    print(best_score)
    if count < best_score:
        best_score = count
        # if count > 6: 
        #     print("To many tries.")
        # else: 
        #     print("Well Done! You found my number in ", count, "tries") 
    
guessing_game()  
print(best_score)
play_again = input("Would you like to play again? Y or N")
if play_again == "Y":
    guessing_game()
else:  
    print(f"See you next time! Your best score is {best_score}")


