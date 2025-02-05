# File: WordleAssistant.py
# Student: Tomas Chang
# 
# Date: 04/15/2022
# Description of Program: This program contains functions required to filter words for a game of wordle

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


def containsAll(wordlist, include):
    """ Given your wordlist, return a set of all words from the wordlist
    that contain all of the letters in the string include.  
    """
    words = set()
    for word in wordlist:
        for i in range(len(include)):
            if include[i] in word:
                append = False
            else:
                append = True
                break
        if append == False:
            words.add(word)
    return(words)

def containsNone(wordlist, exclude):
    """ Given your wordlist, return a set of all words from the wordlist
    that do not contain any of the letters in the string exclude.  
    """
    words = set()
    for word in wordlist:
        for i in range(len(exclude)):
            if exclude[i] not in word:
                append = False
            else:
                append = True
                break
        if append == False:
            words.add(word)
    return(words)

def containsAtPositions(wordlist, posInfo):
    """ posInfo is a dictionary that maps letters to positions.
    You can assume that the positions are in [0..4].  Return a set of
    all words from the wordlist that contain the letters from the
    dictionary at the indicated positions. For example, given posInfo
    {'a': 0, 'y': 4}.   This function might return the set:
    {'angry', 'aptly', 'amply', 'amity', 'artsy', 'agony'}. """
    words = set()
    for word in wordlist:
        for key in posInfo:
            val = posInfo[key]
            if word[val] == key:
                append = False
            else:
                append = True
                break
        if append == False:
            words.add(word)
    return(words)
        

def getPossibleWords(wordlist, posInfo, include, exclude):
    """ Finally, given a wordlist, dictionary posInfo, and
    strings include and exclude, return the set of all words from 
    the wordlist that contains the words that satisfy all of 
    the following:
    * has letters in positions indicated in posInfo
    * contains all letters from string includex
    * contains none of the letters from string exclude.
    """
    containset = containsAll(wordlist, include)
    containlist = list(containset)
    positionset = containsAtPositions(containlist, posInfo)
    positionlist = list(positionset)
    final = wordSet = containsNone(positionlist, exclude)

    return(final)

    