# ***Game Implementation***

Each game is defined as three functions and a string. `generateWords()` returns a list of words to act as a prompt for the player and to be used in scoring. `scoring(promptWords, ansList, timeTaken)` returns a score based on the prompt words, answer words, and time taken. `displayWords(words)` returns a formatted version of the prompt words to be shown to the player. The string `instructions` is the instructions to be shown to the player.

Defining games in this way is done to minimize redundant code and allow new games to be easily added.

Both the singleplayer and multiplayer game runner function take these four items, run the game, and print the score. In multiplayer mode, the game is run as an interactive TCP server on port 1224 and waits for both players to connect before starting. 