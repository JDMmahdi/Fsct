import random

answer = random.randint(1,99)

answer = int(answer)

guess = input("Please enter your guess (between 1 to 99) : ")

guess = int(guess)

while guess != answer:
    if guess > answer:
        print("Your guess is greater than the answer.Please enter it again : ")
    else:
        print("Your guess is lower than the answer.Please enter it again : ")
    guess = input("Please enter you guess : ")
    guess = int(guess)

if guess==answer:
    print("Congrats!!! You guessed it right. :)")