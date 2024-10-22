import sys
import os

# Set path for the create file to create
path = '/home/mnguyen/Development/nguyen-michael-training/Projects/newlist.txt'

# Function saves the current list to a file
def saveList():
    # Check of if the file exists, otherwise create one
    if os.path.isfile(path):
        print('File exists already.')
    else:    
        with open("newlist.txt", 'w') as f:
            for item in taskList:
                f.write("{}\n".format(item))

# Function reads saved file and sets the saved list to the current list
# def pullList():
#     with open('newlist.txt', 'r') as fp:
#         for item in fp:
#             #print("Item", item + 1, ": ", tempList[item], "\n")
#             print(item)

# Function iterates through the list and print each item
def printList():
    for item in range(len(taskList)):
            print("Item", item + 1, ": ", taskList[item], "\n")

# Function returns a boolean for checking the list
def checkList():
    if not taskList:
        return False 
    else:
        return True

# Function takes user input and adds it to the list
def addTasktoList(task):
    taskList.append(task)
    return "\nTask was added to the list successfully!\n"

# Function checks user input and runs appropriate functions
def checkInput(UInput):
    # Check if the user wants to view the list, add to it, or exit
    if(UInput == 1):
        # Check if the list is empty or not
        checkList()
        if checkList() == False:
            print("\nList is empty.\n")
        else:
            printList()
    # Add task and print success message
    elif(UInput == 2):
        addTask = input("\nPlease enter a task to add to the list: \n")
        print(addTasktoList(addTask))
    # Save the list to a file
    elif(UInput == 3):
        saveList()
        print("\nList saved successfully!\n")
    # Pull the saved list from a file
    # elif(UInput == 4):
    #     pullList()
    #     print("\nList successfully pulled!\n")
    # Exit the program
    elif(UInput == 5):
        print("\nExiting Program...\n")
        sys.exit()

# Initialize the list
global taskList
taskList = []

# Ask user for input unitl a vaild input has been made
while True:
    # Check for valid input
    try:
        ask = int(input("Main Menu:\n\nEnter 1 to view the current list.\nEnter 2 to add a task to current list.\nEnter 3 to save the list.\nEnter 5 to exit this program.\n\nUser Input: "))
        # Check user input and call appropriate function
        checkInput(ask)
    except (ValueError, OSError):
        print("\nInvalid input!\n")

       