# File: Wordle.py
# Student: Tomas Chang
# 
# Date: 5/2/2022
# Description of Program: This program aims to allow the user to play the popular game: wordle. The user will need to create a list of words that 
# will be used for the program. 

import os.path
import random

def createWordlist(filename): 
    """ Read words from the provided file and store them in a list.
    The file contains only lowercase ascii characters, are sorted
    alphabetically, one word per line. Filter out any words that are
    not 5 letters long, have duplicate letters, or end in 's'.  Return
    the list of words and the number of words as a pair. """


    newfile = open(filename)
    strippedword = newfile.readline()
    nospaceword = strippedword.rstrip('\n')
    word = nospaceword.rstrip(' ')
    wordlist = []
    count = 0
    while word:
        append = True
        if len(word) == 5:
            if word[-1] != "s":
                append = False
                for i in range(5):
                    for j in range(0,5):
                        if word[j] == word[i] and j != i:
                            append = True
                if append == False:
                    wordlist.append(word)
                    count += 1
        newword = newfile.readline()
        strippedword = newword.rstrip("\n")
        word = strippedword.rstrip(" ")

    return(wordlist, count)   
    
def BinarySearch ( lst , key ):
# """ Search for key in sorted list lst . """
    low = 0
    high = len ( lst ) - 1
    while ( high >= low ):
        mid = ( low + high ) // 2
        if key < lst [ mid ]:
            high = mid - 1
        elif key == lst [ mid ]:
            return mid
        else :
            low = mid + 1
    # What ’s true here ? Why this value ?
    return (- low - 1)

def welcomeMessage():
    print("Welcome to WORDLE, the popular word game. The goal is to guess a")
    print("five letter word chosen at random from our wordlist. None of the")
    print("words on the wordlist have any duplicate letters.\n")
    print("You will be allowed 6 guesses. Guesses must be from the allowed")
    print("wordlist. We'll tell you if they're not.\n")
    print("Each letter in your guess will be marked as follows:")
    print("   x means that the letter does not appear in the answer")
    print("   ^ means that the letter is correct and in the correct location")
    print("   + means that the letter is correct, but in the wrong location\n")
    print("Good luck!\n")


def playWordle(value = None):
    welcomeMessage()
    mm = True
    
    while ( mm == True):
        file = str(input("Enter the name of the file from which to extract the wordlist: "))
        if os.path.isfile(file) == False:
            print("File does not exist. Try again!")
        else:
            newList, length= createWordlist(file)
            mm = False
    if value == None:
        value = random.choice(newList)  
    else:
        if value in newList:
            value.lower()
        else:
            print("")
            print("Answer supplied is not legal.")
            exit()
    guesses=1
    while (guesses <= 6):
        string = 'Enter your guess ('+ str(guesses) + '): '
        guess = str(input(string))
        guess = guess.lower()
        
        if guess in newList:
            print()
            placeholder(guess, value) 
            guesses += 1 
            
        else:
          print("Guess must be a 5-letter word in the wordlist. Try again!")
        if guesses == 7:
          print("")
          print("Sorry! The word was", value ,". Better luck next time!")
        if guess == value:
          print("")
          print("CONGRATULATIONS! You win!")
          break
        
        
#F  R  A  N  K  
#^  ^  ^  ^  ^  
def placeholder(guess, value):
    if guess[0] not in value:
        first = 'x'
    else: 
        first = '+'
        if guess [0] == value[0]:
            first = '^'
          
    if guess[1] not in value:
        second = 'x'
    else:
        second = '+'
        if guess [1] == value [1]:
            second = '^'
      
    if guess [2] not in value:
        third = 'x'
    else:
        third = '+'
        if guess [2] == value [2]:
            third = '^'
          
    if guess [3] not in value:
        fourth = 'x'
    else:
        fourth = '+'
        if guess [3] ==value [3]:
            fourth = '^'

    if guess [4] not in value:
        fifth = 'x'
    else:
        fifth = '+'
        if guess [4] == value [4]:
            fifth = '^'
    for i in range (len(value)):
        print (guess[i].upper() + " ", end = "")
    print("")
    print (first , second , third , fourth , fifth)
#F  R  A  N  K  
#^  ^  ^  ^  ^  
playWordle()
