# Some needed modules for this program:
import turtle
import os

wantsToPlay = True
while wantsToPlay == True:

# Welcomes the user to the program
    print("Welcome to Tucker! \n")

# Needed for my infinite, but breakable, while-loop, and to create the shape
    sides = 0

# The while-loop that make sure the user has a shape from 3 - 10 sides
    while sides < 3 or sides > 10:
        sides = int(input("Enter the number of sides in your shape(3 - 10 sides): "))
        if sides < 3:
            print("Your shape needs at least 3 sides.\n")
        elif sides > 10:
            print("Your shape can't have more than 10 sides.\n")

# This is the list of shapes we will need to check against the user's input, and tells us what shape we will be making
    listOfShapes = ['triangle', 'rectangle', 'pentagon', 'hexagon', 'heptagon', 'octagon', 'nonagon', 'decagon']
    shape = listOfShapes[sides - 3]

# Creates the actual window the shapes will be drawn on with a resolution of 1000x1000 pixels
    myWindow = turtle.Screen()
    myWindow.setup(1000, 1000)

# Names my turtle Tucker and creates him and makes him slower
    Tucker = turtle.Turtle()
    Tucker.speed('slow')

# Creates my angle variable to draw the shape
    angle = 360/sides

# Will make Tucker draw the shape we need with turns and motion
    for x in range(sides):
        Tucker.left(angle)
        Tucker.forward(50)

# The User will guess the shape, and it will play one of two sounds depending on if they win or not
    print("Here's your shape!\n")
    answer = str(input("What is this shape? "))

    if answer.lower() == shape:
        os.system('start correct.wav')
        print ("Correct!")
    else:
        os.system('start incorrect.wav')
        print("Incorrect.")

      # Asks the user if they want to play again
	playAgain = str(input("Do you want to play again?"))
	
	if playAgain.lower == "yes":
		wantsToPlay = True
	else:
		wantsToPlay = False
		quit()
