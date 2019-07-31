import sys
sys.path.append("..")
import socket
import threading
import time
import os

import wordGenesUtil as util

# State vals
clients = []
words = (None, None)
gameStarted = False
gameEnded = False
answers = {}
timeTaken = {}

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(600)
            
            threading.Thread(target = self.listenToClient,args = (client,address)).start()
            
    def listenToClient(self, client, address):
        try:
            size = 1024
            print("Client connected from " + str(address))
            clientNum = len(clients)
            clients.append(client)

            if not (len(clients) == 2):
                client.send(b"Waiting for other player to connect...\n")            
                while not len(clients) == 2:
                    continue
                client.send(b"Other player connected!\n\n")
                beginGame()

            startTime = time.time()
            
            winner = False
                
            while True:
        
                answer = client.recv(1024)
                ansPath = answer.decode("utf-8").rstrip().split(" ")
                timeTaken[clientNum] = time.time() - startTime
                if (util.validatePath(ansPath) and ansPath[0] == words[0] and ansPath[-1] == words[-1]):
                    answers[clientNum] = ansPath
                    if len(answers) == 2:
                        endGame()
                    else:
                        client.send(b"Waiting for other player to answer...\n\n")
                else:
                    client.send(b"Invalid path, try again.\n> ")

                
        except:
            print("SOMETHING HAS GONE WRONG. PLEASE TRY AGAIN.")
            os._exit(1)
def beginGame():

    sendToAll("Complete the word ladder as fast as possible\n")
    sendToAll("Write your answer as wordOne wordTwo wordThree etc\n\n")

    time.sleep(3)
    sendToAll("Game begins in\n")
    for i in range(0,3): 
        sendToAll(str(3-i)+ "\n")
        time.sleep(1)
    sendToAll(str(words[0] + " TO " + words[1] + "\n> "))
    gameStarted = True
    print("game started")

def endGame():

    scores = [None, None]

    for i in range(2):
        scores[i] = scorePlayer(answers[i], timeTaken[i])
        print(str(i) + ": " + str(scores[i]))
        

    winnerNum = None
    if scores[0] > scores[1]:
        winnerNum = 0
    elif scores[1] > scores[0]:
        winnerNum = 1
    else:
        sendToAll("Tie!\n")

    if winnerNum is not None:    
        clients[winnerNum    ].send(b"You won")
        clients[1 - winnerNum].send(b"\nYou lost")
    for client in clients:
        client.close()
    os._exit(0)

def scorePlayer(answerPath, timeTaken):

    score4 = hillScore(answerPath)
    
        
    return score4 / (timeTaken * len(answerPath))

def hillScore(path):
    hillScore = 0
    for ind in range(len(path)-1):
        w1s = util.scoreOfWord(path[ind])
        w2s = util.scoreOfWord(path[ind+1])

        diff = w2s - w1s

        hillScore += diff if diff > 0 else diff*2
        print(hillScore)
        
        print(str(w1s) + " " + str(w2s) + " " + str(diff))
    return hillScore

def sendToAll(obj):
    for client in clients:
        client.send(bytes(obj, 'ascii'))
        
if __name__ == "__main__":

    startWord = util.randomWord()
    endWord = util.randomPathWithLength(startWord, 5)[-1]
    words = (startWord, endWord)
    #print(words)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("ready at " + s.getsockname()[0] +":1224")
    s.close()
    ThreadedServer('', 1224).listen()
    