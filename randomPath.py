import loadDict
import findMutations
import random
import sys

fitDict = loadDict.loadDict()

def main():

    startWord = sys.argv[1]
    print(randomPath(startWord))   

def randomPath(startWord):
    curWord = startWord
    path = []
    while True:
        goodPos, badPos = findMutations.possibleMutations(fitDict, curWord)
        path.append(curWord)
        if (len(goodPos) == 0):
            return path
        curWord = random.choice(list(goodPos.keys()))

def randomPathWithLength(startWord, length):
    while True:
        path = randomPath(startWord)
        if (len(path) > length):
            return path

def randomWord():
    return random.choice(list(fitDict.keys()))
    
if __name__ == "__main__":
    main()