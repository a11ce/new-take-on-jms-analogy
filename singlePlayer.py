import sys
sys.path.append("..")
import time
import random

import wordGenesUtil as util


def runGame(generator, scoring, displayPrompt, instructions):
    randomSeed = int(input("Enter shared game number\n> "))
    random.seed(randomSeed)
    
    promptWords = generator()

    print(instructions)
    print("Write your answer as wordOne wordTwo wordThree etc\n")

    time.sleep(1)
    print("Game begins in")
    for i in range(0,3): 
        print(3-i)
        time.sleep(1)
    print()
    
    startTime = time.time()
                
    print(displayPrompt(promptWords), end = "")

    answer = input()
    ansPath = answer.rstrip().split(" ")
    timeTaken = time.time() - startTime

    score = scoring(promptWords, ansPath, timeTaken) 

    print("Your score is:")   
    print(score)
    #print(sortedList)
        
if __name__ == "__main__":
    main()