import loadDict
import findMutations
import random
import sys
def main():
    fitDict = loadDict.loadDict()
    curWord = sys.argv[1]
    while True:
        goodPos, badPos = findMutations.possibleMutations(fitDict, curWord)
        print(curWord + ": " + str(goodPos))
        if (len(goodPos) == 0):
            print("END OF SEQ")
            break
        curWord = random.choice(list(goodPos.keys()))     

if __name__ == "__main__":
    main()