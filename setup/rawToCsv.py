#!/usr/bin/env python3

import os

keepYear = "2000"
keepLength = 4
curWord = "blank"
curCount = 0

dataDir = "../data/raw1gram/"
for filename in os.listdir(dataDir):
    if not filename.endswith("gz"):
        with open((dataDir + filename)) as inFile:
            
            for line in inFile:
                lineSplit = line.split("\t")
                #print(lineSplit)
                if(lineSplit[1] == keepYear):
                    word = line.split("\t")[0]
                    word = word.split("_")[0]
                    word = word.split(".")[0]
                    word = word.lower()
                    
                    if(word != curWord and len(word) == keepLength):
                        print(curWord + "," + str(curCount))
                        curWord = word
                        curCount = int(lineSplit[2])
                    elif(len(word) == keepLength):
                        curCount += int(lineSplit[2])
                        
                        
                 