import random

import randomPath
import loadDict

def main():

    fitDict = loadDict.loadDict()
    corCount = 0
    print("Type the more common word\n")
    print()
    for _ in range(15):
        if(askOne(fitDict)):
            corCount += 1
        print()
    print("You got " + str(corCount) + "/15")
    
def askOne(fitDict):
    seedWord = random.choice(list(fitDict.keys()))
    while True:
        path = randomPath.randomPath(seedWord, fitDict)
        if len(path) > 4:
            break
    corWord = path[-1]
    inCor   = path[-2]
    
    if random.choice([True, False]):
        print(corWord + " or " + inCor)
    else:
        print(inCor + " or " + corWord)

    response = input()
    if response == corWord:
        return True
    return False

if __name__ == "__main__":
    main()