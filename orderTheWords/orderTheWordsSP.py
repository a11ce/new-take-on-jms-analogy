import sys
sys.path.append("..")
import singleplayer
import random
import wordGenesUtil as util

def generateList():
    words = []
    sortedWords = []
    for _ in range(4):
        words.append(util.randomPathWithLength(util.randomWord(),2)[-1])
    for word in util.sortList(words)[::-1]:
        sortedWords.append(word)
    return sortedWords
    
def scoring(sortedList, ansPath, timeTaken):
    wordsCorrect = 0
    for i in range(len(ansPath)):
        if ansPath[i] == sortedList[i]:
            wordsCorrect += 1
    score = int((wordsCorrect / timeTaken) * 1000)
    return score

def displayWords(sortedList):
    returnString = ""
    for word in random.sample(sortedList, len(sortedList)):
        returnString += word + " "
    returnString += "\n> "

    return returnString

singlePlayer.runGame(generateList, scoring, displayWords, "Order the words from most to least common")