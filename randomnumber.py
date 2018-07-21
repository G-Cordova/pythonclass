from random import randint

guess = input("Please enter your guess here.")
random_number = randint(1,10)

while guess != random_number:
    if guess != random_number:
        print("BEEP! Wrong.")
    elif guess == random_number:
        print("YASSS!")
