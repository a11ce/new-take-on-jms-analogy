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

    def hillScore(path):
        hillScore = 0
        for ind in range(len(path)-1):
            w1s = util.scoreOfWord(path[ind])
            w2s = util.scoreOfWord(path[ind+1])
            diff = w2s - w1s
            hillScore += diff if diff > 0 else diff*2
        return hillScore

    if (util.validatePath(ansPath) and ansPath[0] == words[0] and ansPath[-1] == words[-1]):
        return int((hillScore(ansPath) / (timeTaken * len(ansPath))) /10 )
    else:
        print("Invalid path!")
        return float('inf') * -1


def displayWords(words):
    return str(words[0] + " TO " + words[1] + "\n> ")

singlePlayer.runGame(generateWords, scoring, displayWords, "Complete the word ladder as fast as possible and also mostly uphill")