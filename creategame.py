#This program creates a window using tkinter and allows the user to dynamically update
# the size of that window by adjusting guess and answer inputs

# tkinter is a library for creating simple GUIs (Graphical User Interfaces AKA windows)
# http://effbot.org/tkinterbook/
# http://usingpython.com/using-tkinter/
import tkinter
from random import randint

# Define the starting size of the window, we will use this in a couple places
STARTING_HEIGHT = 400
STARTING_WIDTH = 400

target = randint(1,1000)


# Display the area of the GUI window
def setAreaText(label, area):
    label.configure(text="Looking for " + str(target) + " number")

# Calculate an area
def calculateArea(guess, answer):
    return guess * answer

# Create a GUI window with tkinter
window = tkinter.Tk()

# Set the initial title and dimensions of the GUI window
window.title("Pick a number")
window.geometry("400x400")

# Create a label and input for the guess property
widthLabel = tkinter.Label(window, text="Number:")
widthLabel.grid(row=0, column=0)
usersGuessedNumber = tkinter.Entry(window)
usersGuessedNumber.grid(row = 0, column = 1, columnspan = 2)
usersGuessedNumber.insert(0, STARTING_WIDTH)


# Create a label for displaying the area of the window
answerLabel = tkinter.Label(window)
answerLabel.grid(row=2, column=0, columnspan=3)
setAreaText(answerLabel, calculateArea(STARTING_WIDTH, STARTING_HEIGHT))

# A function that is executed when the button is pressed
# tell user if guess is right or wrong
def guessANumber():
    guess = int(usersGuessedNumber.get())
    answerLabel.configure(text="Looking for" + str(target) + " given " + str(guess))
    if target < guess:
        answerLabel.configure(text="You guessed too high!")
    elif target > guess:
        answerLabel.configure(text="You guessed too low!")
    else:
        answerLabel.configure(text="You got it!")

# Create a button that will apply the updated guess and answer.
# When the button is pressed, the command to execute 
changeWindowSizeButton = tkinter.Button(window, text="Make a guess!", command=guessANumber)
changeWindowSizeButton.grid(row=3, column=1)

#Start the GUI window
window.mainloop()
