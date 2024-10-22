import sys
import random

# Validate user input
def isValidInput(uInput):
    # Strip the input of any whitespace
    newString = uInput.strip()
    
    # Check if the input is a valid integer
    try:
        if int(newString):
          return int(newString)
    except ValueError:
        print("Invalid Input")

class flashcard:
    # Initialize the fruits for the flashcards
    def __init__(self):  
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow',
                     'Blueberry':'blue',
                     'strawberry':'red',
                     'coconut':'brown',
                     'pomelo':'yellow',
                     'starfruit':'yellow'}
    # Initialize the Quiz    
    def quiz(self):
        # Prompt user continuously
        while (True):
            # Set the flashcards
            fruit, color = random.choice(list(self.fruits.items()))
            
            print("What is the color of {}".format(fruit))
            ask = input()
            
            # Check the answer from the user
            if(ask.lower() == color):
                print("\nCorrect answer\n")
            else:
                print("\nWrong answer\n")

            # Prompt the user to play again    
            try:
                option = input("Enter 0 if you want to play again; Otherwise press enter to exit : ")
                if (option == "0"):
                    continue
                elif(option == ""):
                    print("Exiting program...")
                    sys.exit()
            except ValueError:
                print("Invalid input.")

# Prompt user for input
userInput = input("\n---Main Menu---\n\nEnter 1 to try the flashcards.\nEnter 2 to exit the program.\n\nInput: ")
# Check input
if isValidInput(userInput) == 1:
    # Call randomizer and display flashcards
    fc=flashcard()
    fc.quiz()

elif isValidInput(userInput) == 2:
    print("Exiting program...")
    sys.exit()