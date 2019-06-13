import sys
sys.path.append("..")
import wordGenesUtil as util
import socket
import threading
import time

# State vals
clients = []
words = (None, None)
gameStarted = False
gameEnded = False

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
        print("Waiting for inp")

        winner = False
                
        while True:
        
            answer = client.recv(1024)
            ansPath = answer.decode("utf-8").rstrip().split(" ")
            if(util.validatePath(ansPath) and ansPath[0] == words[0] and ansPath[-1] == words[-1]):
                endGame(clientNum)
            else:
                client.send(b"No\n> ")
        
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

def endGame(winnerNum):
    clients[winnerNum    ].send(b"You won")
    clients[1 - winnerNum].send(b"\nYou lost")
    for client in clients:
        client.close()

def sendToAll(obj):
    for client in clients:
        client.send(bytes(obj, 'ascii'))
        
if __name__ == "__main__":

    startWord = util.randomWord()
    endWord = util.randomPathWithLength(startWord, 5)[-1]
    words = (startWord, endWord)
    print(words)
    print("ready")
    ThreadedServer('', 1224).listen()
    