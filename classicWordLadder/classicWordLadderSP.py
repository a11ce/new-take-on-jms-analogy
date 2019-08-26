import sys
sys.path.append("..")
import singleplayer
import random
import wordGenesUtil as util

def generateWords():
    startWord = util.randomWord()
    endWord = util.randomPathWithLength(startWord, 5)[-1]
    words = (startWord, endWord)
    return words

def scoring(words, ansPath, timeTaken):
    if (util.validatePath(ansPath) and ansPath[0] == words[0] and ansPath[-1] == words[-1]):
        return int((90 - timeTaken) * 100 / (len(ansPath)*2))
    else:
        print("Invalid path!")
        return float('inf') * -1

def displayWords(words):
    return str(words[0] + " TO " + words[1] + "\n> ")

singlePlayer.runGame(generateWords, scoring, displayWords, "Complete the word ladder as fast as possible")