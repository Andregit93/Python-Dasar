class queue:

    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def enqueue(self, value):
        self.item.insert(0, value)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

import random

def Gacha(players):
    if players is None or len(players) <= 1:
        return players

    simQ = queue()
    plsize = len(players)
    for p in players:
        simQ.enqueue(p)

    while simQ.size() > 1:
        r = random.randint(plsize, plsize*2)
        for i in range(r): 
            simQ.enqueue(simQ.dequeue())
        simQ.dequeue()
    return simQ.dequeue()


def readInput():
    print("Enter player names, comma separated ")
    name = input()
    name_list = name.split(",")
    name_list = [n.strip() for n in name_list]
    return (name_list)


def main():
    player = readInput()
    winner = Gacha(player)
    print("winner is: ", winner)

if __name__ == "__main__":
    main()