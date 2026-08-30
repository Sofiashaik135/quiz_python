import random
print("Welcome to the number guessing game")
print("I am thinking of a number between 1 to 100")
computer_num = random.randint(1,100)
while True:
        guess_num = int(input("guess the number\n"))
        if guess_num == computer_num:
            print("congratulations! you guessed the correct number. ")
            break
        elif guess_num < computer_num:
            print("too low !Try again. ")
        elif guess_num > computer_num:
            print("too high!Try again. ")

     
    


