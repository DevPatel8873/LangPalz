import secrets
import PIL
from PIL import Image

import googletrans
from googletrans import Translator

import random
#import psutil
import time
#import subprocess
#import sys

import threading


emotionsImageList = ["angry.png", "sad.png", "scared.png", "smile.png", "tired.png"]
emotionsAnsList = ["angry", "sad", "scared", "happy", "tired"]

objectsImageList = ["bubbles.png", "camera.png", "computer.jpg", "door.png", "Fish.png", "flower.png", "penguin.png", "shoes.png", "tree.png", "Jacket.png"]
objectsAnsList = ["bubbles", "camera", "computer", "door", "fish", "flower", "penguin", "shoes", "tree", "jacket"]

placesImageList = ["beach.png", "grocery_store.webp", "house.png", "jail.png", "library.jpg", "mountain.jpg", "park.png", "stadium.jpg"]
placesAnsList = ["beach", "grocery store", "house", "jail", "library", "mountain", "park", "stadium"]

allImageList = ["angry.png", "sad.png", "scared.png", "smile.png", "tired.png", "bubbles.png", "camera.png", "computer.jpg", "door.png", "Fish.png", "flower.png", "penguin.png", "shoes.png", "tree.png", "Jacket.png", "beach.png", "grocery_store.webp", "house.png", "jail.png", "library.jpg", "mountain.jpg", "park.png", "stadium.jpg"]
allAnsList = ["angry", "sad", "scared", "happy", "tired", "bubbles", "camera", "computer", "door", "fish", "flower", "penguin", "shoes", "tree", "jacket", "beach", "grocery store", "house", "jail", "library", "mountain", "park", "stadium"]

translator = Translator()
points = 0

global secs 


# def timer():
#     secs = 15

#     for i in range(secs + 1):
#         # displayTimer = "{:02d}:{:02d}".format(0, secs)
#         # print(displayTimer, end="\r")
#         secs = secs - 1
#         time.sleep(1)
        

def mainMenu():#main menu directory
    print("...................LangPalz................")
    print()

    choice = ""

    while(choice == ""):
        choice = input("""
                        A: Normal Mode
                        B: Multiple Choice Mode
                        C: Zen Mode
                        D: Exit

                        Please enter your choice: """)

        choice.lower()

        if choice == "a":
            return chooseCategory()
        elif choice == "b":
            return multipleChoice(points)
        elif choice == "c":
            return zenMode(points)
        elif choice == "d":
            return 0
        else:
            print("You must only select either A, B, C or D")
            print("Please try again")
            choice = ""

def chooseCategory():#expression, object and places directory
    choice = ""
    while(choice == ""):
        choice = input("""
                        A: Emotions
                        B: Objects
                        C: Places
                        D: Mixed

                        Please enter your choice: """)

        choice.lower()
    
        if choice == "a":
            return normalMode(emotionsImageList, emotionsAnsList, points)
        elif choice == "b":
            return normalMode(objectsImageList, objectsAnsList, points)
        elif choice == "c":
            return normalMode(placesImageList, placesAnsList, points)
        elif choice == "d":
            return normalMode(allImageList, allAnsList, points)
        else:
            print("You must only select either A, B, or C")
            print("Please try again")
            choice = ""

def normalMode(imgList, ansList, pnts): 

    index = random.randint(0, len(imgList) - 1)

    image = Image.open(imgList[index])
    image.show()


    userInput = input("Enter your guess: ")
    userInput = translator.translate(userInput).text #translates to english

    userInput.lower()

    if(userInput == ansList[index]):
        print("Correct!\n")
        return (pnts+1)
    else:
        print("Incorrect\n Correct answer was: " + ansList[index])
        return pnts

def zenMode(pnts):
    # countdown_thread = threading.Thread(target = timer)
    # countdown_thread.start()
    # secs = 15
    while True:
        
        index = random.randint(0, len(allImageList) - 1)

        image = Image.open(allImageList[index])
        image.show()
    

        print()
        userInput = input("Enter your guess (enter 1 to quit): ")
        userInput = translator.translate(userInput).text #translates to english

        userInput.lower()

        if(userInput == allAnsList[index]):
            print("Correct!\n")
            pnts = pnts + 1
            #secs = secs + 2
        elif(userInput == "1"):
            return pnts
        else:
            print("Incorrect\n")

def multipleChoice(pnts):
    for key, value in googletrans.LANGUAGES.items():
        print(key, ' = ', value)
    
    
    language = ""
    exists = False

    while(language == "" and exists == False):
        language = input("Enter the language you want to play in(abbreviation only): ")

        language.lower()

        for key in googletrans.LANGUAGES:
            if(language == key):
                exists = True
                break
        
        if(exists == False):
            print("Invalid language please enter again")
            language = ""

    correctIndex = random.randint(0, len(allImageList) - 1)

    randChoice1 = random.randint(0, len(allImageList) - 1)
    randChoice2 = random.randint(0, len(allImageList) - 1)
    randChoice3 = random.randint(0, len(allImageList) - 1)

    choices = [allAnsList[randChoice1] , allAnsList[randChoice2], allAnsList[randChoice3], allAnsList[correctIndex]]

    copyChoices = [allAnsList[randChoice1] , allAnsList[randChoice2], allAnsList[randChoice3], allAnsList[correctIndex]]

    image = Image.open(allImageList[correctIndex])
    image.show()

    choiceCount = 1

    for i in range(4):
        displayRand = random.randint(0, len(choices) - 1)
        translatedChoice = translator.translate(choices[displayRand], src='en', dest=language).text
        print(str(choiceCount) + ") " + translatedChoice)
        choices.pop(displayRand)
        choiceCount = choiceCount + 1

    userGuess = 0
    while(userGuess == 0):
        userGuess = int(input("Select which choice is the correct word that matches the picture(number 1 to 4): "))
        for i in range(1, 5):
            if(userGuess == i):
                if(copyChoices[i - 1] == allAnsList[correctIndex]):
                    print("Correct\n")
                    return pnts + 1
                else:
                    print("Incorrect\n Correct answer was: " + allAnsList[correctIndex])
                    return pnts

        print("Invalid choice please select again")
        userGuess = 0


points = mainMenu()


# playAgain = ""

# while playAgain == "":
#     points = mainMenu()
#     print("Points: " + str(points))
#     playAgain = input("Play Again?(Y or N): ")

#     if(playAgain == "Y"):
#         playAgain = ""
#     else:
#         break

print("Total Points: " + str(points))