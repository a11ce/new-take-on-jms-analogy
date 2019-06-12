import loadDict
import findMutations
import random
import sys
def main():
    fitDict = loadDict.loadDict()
    startWord = sys.argv[1]
    print(randomPath(startWord, fitDict))   

def randomPath(startWord, fitDict):
    curWord = startWord
    path = []
    while True:
        goodPos, badPos = findMutations.possibleMutations(fitDict, curWord)
        path.append(curWord)
        if (len(goodPos) == 0):
            return path
        curWord = random.choice(list(goodPos.keys()))
    

if __name__ == "__main__":
    main()