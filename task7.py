import random 


class player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        sub = 0

    def __call__(self, name):
        print("it broken")
    def throwDice():
        x = random.random(1, 6)
        y = random.random(1, 6)
        if(x and y == 1):
            total = 0
            sub = 0
        elif(x or y == 1):
            sub == 0
        else:
            sub += x+y
    def Hold():
        total += sub
        sub = 0
    def Pass():
        sd

class game:
    def __init__(self, name, target):
        player1 = player(name)
        self.player2 = player(input("enter second player: "))
        player3 = ""
        player4 = ""
        player5 = ""
        self.PlayerList = [player1, self.player2]
        self.target = target


    def addPlayer():
        self.PlayerList.append(player(input("Enter player name: ")))

    def turn(self, current):
        print(self.PlayerList[current].name + "'s turn")
        while(True):
            action = input("Play your move: \n")
            if(action == "roll" or "r"):
                player1.throwDice()
                if(player1.sub == 0):
                    break
            if(action == "hold" or "h"):
                self.player1.Hold()
                break
            if(action == "pass" or "p"):
                self.player1.Pass()
                break
    def play(self):
        self.victory = False
        current = 0
        while(not self.victory):
            print("playing")
            if(current == len(self.PlayerList) ):
                print("Score: \n" +self.player1.name +self.player1.total + ": ""\n"+self.player2.name +": " + self.player2.total)
                break
            else:
                self.turn(current)
                current += 1
    
tmp = game(input("Enter player name: "),int(input("Enter target ammount: ")))
game.play(tmp)