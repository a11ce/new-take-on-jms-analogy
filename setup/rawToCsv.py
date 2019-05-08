#!/usr/bin/env python3

import os
import re
from tqdm import tqdm
import sys

#keepYears = ["1800", "1850", "1900","1950","2000"] 
#keepYears  = ["1950"]
keepLength = 4
curWord = "blank"
curCount = 0
keepYear = sys.argv[1]

dataDir = "../data/raw1gram/"
lettersRe = re.compile('[^a-zA-Z]')
freqDict = {}

for filename in os.listdir(dataDir):
    
    if not filename.endswith("gz"):
        with open((dataDir + filename)) as inFile:
            
            for line in inFile:
                lineSplit = line.split("\t")
                #print(lineSplit)
                if(lineSplit[1] == keepYear):
                    word = lineSplit[0]
                    word = word.split("_")[0]
                    word = word.split(".")[0]
                    word = lettersRe.sub('', word)
                    word = word.lower()
                    
                    if(len(word) == keepLength):
                        if(word in freqDict):
                            freqDict[word] += int(lineSplit[2])
                        else:
                            freqDict[word] = int(lineSplit[2])

for key, value in freqDict.items():
    print(key + "," + str(value))
                 