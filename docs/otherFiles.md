# ***Utility Files and Functions***

## `loadDict.py` 

This file contains one function, `loadDict()`, which loads the `word:fitness` data from a hardcoded CSV (currently `/data/csv/filtered-2000.csv`) and returns it as a python dict.

## `findPath.py`

This file is not used anywhere, and is run with `python3 findPath.py startWord endWord`. It will look for a single uphill path from startWord to endWord, which does not always exist. It also does not always find the shortest path. If an empty `[]` is printed, there is no uphill path possible, even though the end word is more common than the start word.

## `findMutations.py`

This file contains one function to find the possible mutations one step away from a word. It returns two dicts, both of the format `word:fitness`. goodPos is a dict of uphill possible words, and badPos is of downhill words. It is used in `wordGenesUtil`.

## `wordGenesUtil.py`

This is the only utility file meant to be imported. 

It contains the following functions:

#### `randomPath(startWord)`

Returns an uphill path starting at startWord and ending at a local maximum word.

#### `randomPathWithLength(startWord, minLength)`

Returns a path from randomPath with a length greater or equal to minLength. Known issue: If no path long enough exists, it will result in an infinite loop.

#### `randomWord()`

Returns a random word from the dataset.

#### `scoreOfWord(word)`

Returns the fitness score of the given word.

#### `validatePath(path)`

Returns true if the path is valid: 
- Each word in the path is in the dataset
- Each word except the first can be made by changing one letter of the previous word.

or false otherwise.

#### `sortList(wordList)`

Returns the given list sorted from least to most common.
