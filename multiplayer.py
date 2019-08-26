import socket
import threading
import time
import os
import traceback

import wordGenesUtil as util

clients = []
promptWords = None
gameStarted = False
gameEnded = False
answers = {}
timeTaken = {}

scoring = None
displayPrompt = None
instructions = None

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
                answers[clientNum] = ansPath
                timeTaken[clientNum] = time.time() - startTime
                if len(answers) == 2:
                    endGame()
                else:
                    client.send(b"Waiting for other player to answer...\n\n")
        except Exception as e:
            print(traceback.format_exc())
            os._exit(1)

def beginGame():
    sendToAll(instructions + "\n")
    sendToAll("Write your answer as wordOne wordTwo wordThree etc\n\n")

    time.sleep(3)
    sendToAll("Game begins in\n")
    for i in range(0,3): 
        sendToAll(str(3-i)+ "\n")
        time.sleep(1)
    sendToAll("\n")

    sendToAll(displayPrompt(promptWords))

    gameStarted = True
    print("Game started")

def endGame():
    print("Game ended")
    scores = [None, None]

    for key, val in answers.items():
        scores[key] = scoring(promptWords, val, timeTaken[key])
        print("player " + str(key) + " score is " + str(scores[key]))

    winnerNum = None
    if scores[0] > scores[1]:
        winnerNum = 0
    elif scores[1] > scores[0]:
        winnerNum = 1
    else:
        sendToAll("Tie!\n")

    if winnerNum is not None:
        clients[winnerNum    ].send(b"You won!\n")
        clients[1 - winnerNum].send(b"\nYou lost!\n")

    for client in clients:
        client.close()
    os._exit(0)

def sendToAll(obj):
    for client in clients:
        client.send(bytes(obj, 'ascii'))

def runGame(generator, inSc, inDiPr, inIn):
    global promptWords
    promptWords = generator()
    global scoring
    scoring = inSc
    global displayPrompt
    displayPrompt = inDiPr
    global instructions
    instructions = inIn
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("ready at " + s.getsockname()[0] +":1224")
    s.close()
    ThreadedServer('', 1224).listen()