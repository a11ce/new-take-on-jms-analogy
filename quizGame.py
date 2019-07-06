import random

import wordGenesUtil as util

def main():

    corCount = 0
    print("Type the more common word\n")
    print()
    for _ in range(15):
        if(askOne()):
            corCount += 1
        print()
    print("You got " + str(corCount) + "/15")
    
def askOne():
    seedWord = util.randomWord()
    path = util.randomPathWithLength(seedWord,4)
    corWord = path[-1]
    inCor   = path[-2]
    
    if random.choice([True, False]):
        print(corWord + " or " + inCor + "\n> ", end = '')
    else:
        print(inCor + " or " + corWord + "\n> ", end = '')

    response = input()
    if response == corWord:
        return True
    return False

if __name__ == "__main__":
    main()