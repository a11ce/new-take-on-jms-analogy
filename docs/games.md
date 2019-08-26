% Word Genes

# ***Games***

## Classic Word Ladder
Word ladder, invented by Lewis Carroll, is a puzzle in which a player is given two words. The player must transform one word to the other by means of single letter substitution, where all substitutions must result in a word. 

One of Carroll's examples is as follows:
```head 
heal 
teal 
tell 
tall 
tail```

Notably different from our randomly generated ladders, Carroll's start and end words had some sort of connection, used in phrasing the puzzle. One of the few three-letter prompts was "Evolve MAN from APE."

The original method of scoring was published in Vanity Fair as follows:

"Each competitor, who completes the Chain with the least possible number of Links, will receive the full number of marks assigned; and each who uses more than the least possible number of Links will lose a mark for every additional Link."

In order to incorporate the time taken in our scoring system, we use the following function:

`score(timeTaken, path) = ((90-timeTaken) * 100) / (length(path)*2)`

The constants (and the function itself) are entirely arbitrary and chosen to give reasonable changes when time and length vary.

## Bridge the Gap

This mode is similar to Classic Word Ladder, except for the scoring, which is as follows:

The hill score of a path (`hillScore(path)`) is the sum of the fitness differences between each adjacent pair of words in the path with negative differences doubled.

`score(timeTaken, path) = (hillScore(path) / (timeTaken * length(path)) / 10`

The score function is again arbitrary. The hill score rewards uphill paths in order to mirror evolution. 

## Order the Words

In Order the Words, the player is given four words in a random order and must order them from most to least common as fast as possible.

Score is given by `(wordsCorrect / timeTaken) * 1000`, where wordsCorrect is given by the count of when answerList[i] is the same as sortedList[i] for i, each index in the lists.

## Quiz Game

There is also a singplayer-only quiz game not defined in the Word Genes spec. It prints two words and asks the player to enter the more common one, five times. At the end, it prints how many the player answered correctly.

