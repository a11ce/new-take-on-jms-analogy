import sys
sys.path.append("..")
import socket
import threading
import time
import os
import random

import wordGenesUtil as util

# State vals
clients = []
sortedList = []
gameStarted = False
gameEnded = False
answers = {}

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

            winner = False
                
            while True:
        
                answer = client.recv(1024)
                ansPath = answer.decode("utf-8").rstrip().split(" ")
                answers[clientNum] = ansPath
                if len(answers) == 2:
                    endGame()
                else:
                    client.send(b"Waiting for other player to answer...\n\n")
        except Exception as e:
            print(e)
            print("SOMETHING HAS GONE WRONG. PLEASE TRY AGAIN.")
            os._exit(1)
def beginGame():

    sendToAll("Order the words from most to least common\n")
    sendToAll("Write your answer as wordOne wordTwo wordThree etc\n\n")

    time.sleep(3)
    sendToAll("Game begins in\n")
    for i in range(0,3): 
        sendToAll(str(3-i)+ "\n")
        time.sleep(1)
    sendToAll("\n")
    
    for word in random.sample(sortedList, len(sortedList)):
        sendToAll(str(word) + " ")
    sendToAll("\n> ")
    
    gameStarted = True
    print("game started")

def endGame():
    print("game ended")
    scores = [None, None]

    
    for key, val in answers.items():
        score = 0
        for i in range(len(val)):
            if val[i] == sortedList[i]:
                score += 1
        scores[key] = score

    winnerNum = None
    if scores[0] > scores[1]:
        winnerNum = 0
    elif scores[1] > scores[0]:
        winnerNum = 1
    else:
        sendToAll("Tie!")

    if winnerNum is not None:
        clients[winnerNum    ].send(b"You won!\n")
        clients[1 - winnerNum].send(b"\nYou lost!\n")

    sendToAll("Correct order was: ")
    for word in sortedList:
            sendToAll(str(word) + " ")
            
    for client in clients:
        client.close()
    os._exit(0)

def sendToAll(obj):
    for client in clients:
        client.send(bytes(obj, 'ascii'))
        
if __name__ == "__main__":
    
    words = []
    for _ in range(4):
        words.append(util.randomPathWithLength(util.randomWord(), 2)[-1])
    
    for word in util.sortList(words)[::-1]:
        sortedList.append(word)
    print(sortedList)
        
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("ready at " + s.getsockname()[0] +":1224")
    s.close()
    ThreadedServer('', 1224).listen()
    