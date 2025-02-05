# File: Fibonnaci Numbers.py
# Student: Tomas Chang
# Date: 4/24/2022
# Description of Program: This program is aimed to allow the user to perform multiple 
# functions from the fibonnaci numbers. 

def firstNFibNumbers (n):
    """ Return a list of the first n Fibonnaci numbers.  If 
        n < 0, return the empty list. """
    
    if n <= 0:
        return []

    # Handle the cases of n == 1 and n == 2 specially.
    elif n == 1:
        return [ 0 ]
    elif n == 2:
        return [ 0, 1 ]

    # Here we know that n is at least 2.
    else:

        # Initialize fib1 and fib2 with the first 
        # two Fibonnaci numbers.
        fib1, fib2 = 0, 1

        # Initialize our list of Fibonnaci numbers
        # found so far.
        fibs = [ 0, 1 ]

        # Use the previous two values to generate 
        # and record the next value.
        for counter in range( 2, n ):

            # Update fib1 and fib2 with their new
            # values.
            fib1, fib2 = fib2, fib1 + fib2

            # Add the newest value to the list we're
            # creating.
            fibs.append( fib2 )

        return fibs

def guide():
    print("The following commands are available:")
    print(" 0: Exit.")
    print(" 1: List the first N Fibonnaci numbers.")
    print(" 2: Display the ith Fibonnaci number (0-based).")
    print(" 3: List the Fibonnaci numbers less or equal to N.")
    print(" 4: How many Fibonnaci numbers are less or equal to N?")
    print(" 5: Find a list of the largest Fibonnaci numbers that add up to N.")
    print(" 6: Display this help message. ")

def command1():
    looper = True
    command1 = int(input("You've asked for the first N Fibonnaci numbers. What is N? "))
    if (command1 < 0 ):
        print("ERROR: Illegal value entered.")
        looper = False
    else:
        print(firstNFibNumbers (command1))
        looper = False

def command2():
    command2 = int(input("You've asked for the ith Fibonnaci number. What is i? "))
    if (command2 < 0): 
        print("ERROR: Illegal value entered.")
        looper = False
    else:
        list = firstNFibNumbers (command2+1)
        print (list[command2])

def command3():
    command3 = int(input("You've asked for the Fibonnaci numbers less than or equal to N. What is N? ")) 
    if True:
        lessore = firstNFibNumbers (command3+5)
        nlist = []
    for i in range (command3+5):
        if (command3 >= lessore[i]):
            nlist.append(lessore[i])
    print(nlist)
    looper = False

def command4():
    command4 = int(input("You've asked how many Fibonnaci numbers are less than or equal to N. What is N? "))
    if True:
        count = 0
        nlist = []
        list= firstNFibNumbers (command4+5)
                
    for i in range (command4+5):
        if list[i] <= command4:
            count += 1
    print(count)
    looper = False 

def command5():
    command5 = int(input("You've asked for Fibonnaci numbers that sum to N. What is N? "))
    if (command5 < 0):
        print("ERROR: Illegal value entered.")
        looper = False
    else:
        list = firstNFibNumbers (command5+10)
        answer = []
        nlist = []
        for i in range (command5+10):
            if list[i] <= command5:
                nlist.append(list[i])
            if command5 == 0:
                answer.append(0)
                print(answer)
                looper = False
                break    

        for y in range (-1, -1*len(nlist), -1):
            if nlist[y] <= command5:
                command5-= nlist[y]
                answer.append(nlist[y])
        print(answer)
        looper = False
        
def command6():
    guide()
    looper = False


def fibnums():
    
    print("")
    print('Welcome to the Fibonnaci Number laboratory!\n')
    guide()
    o = -1
    while o!= 0:
        looper = True
        print("")
        command = int(input("Please enter a command (0, 1, 2, 3, 4, 5 or 6): "))
        if (command > 6 or command < 0):
            print ("ERROR: Illegal value entered.")

        elif (command == 0):
            print("")
            print("Thanks for using the Fibonnaci Laboratory! Goodbye.\n")
            break

        elif command == 1 and looper == True:
            command1()
        
        elif looper == True and command == 2:
            command2()

        elif looper == True and command == 3:
            command3()
                
        elif looper == True and command == 4:
            command4()
            
        elif looper == True and command == 5:
            command5()
            
        elif looper == True and command == 6:
            command6()

fibnums()