import random

class Player():
    def __init__(self, id, bank):
        self.id = id
        self.hand = []
        self.fold = False # need to reset to true with conditions
        # self.check = False
        # self.raises = False
        self.bank = bank

    def playerChoice(self, playerObj):
        # return fold, check, raises, or pass
        # ai choice

        if playerObj.fold == False:
            choiceTemp = random.randchoice(["fold", "check", "raises"]) # 1/3 dice roll
            if choiceTemp == "fold":
                playerObj.fold = True
            return choiceTemp
        else:
            return "pass"

# does all the things required for the table, including fielding players, players hands, and table cards
# turns 0:  player choice: fold, call, raises
# turn 1.a: player choice: fold, check, raises
# turn 1.b: table reveal 3 cards (3 total)
# turn 2.a: player choice: fold, check, raises
# turn 2.b: table reveal 1 card (4 total)
# turn 3.a: player choice: fold, check, raises
# turn 3.b: table reveal 1 card (5 total)
# turn n:   player choice: fold, check, raises

class Table():
    def __init__(self, nPlayers, deckList):
        self.nPlayers = nPlayers
        self.playerList = []
        self.tableList = []
        self.deckList = deckList
        self.minBet = 2 # mutable number that changes as players bet more
        self.pot = 0
        # all in scenios

    def genPlayers(self):
        for i in range(self.nPlayers):
            self.playerList.append(Player(i, 1000)) # initial moneys

    def genPlayerHands(self):
        for playerHand in self.playerList:
            for _ in range(2):
                tempCard = self.deckList.drawDeck.pop()
                playerHand.hand.append(tempCard)

    # reveal slowly, split into 2 functions
    def genTableInitial(self):
        for _ in range(3):
            tempCard = self.deckList.drawDeck.pop()
            self.tableList.append(tempCard)

    # will be called twice, slow reveal
    def genTableTwo(self):
        tempCard = self.deckList.drawDeck.pop()
        self.tableList.append(tempCard)

    def printTable(self):
        print(" --*--*--*--*--*--*--* table *--*--*--*--*--*--*--* ")
        for i in self.tableList:
            print(f"{i.rank} {i.suit}", end='   ')
        print("")
        print("----------------------------------------------------")

    def printPlayerHands(self):
        for player in self.playerList:
            print(f"player {player.id}: ", end='')
            for playerHand in player.hand:
                print(f"{playerHand.rank} {playerHand.suit}", end='   ')
            print("")

class Card():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value

class Deck():
    def __init__(self):
        self.drawDeck = []

    def genDeck(self):
        list_rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        list_suit = ["Clubs", "Hearts", "Spade", "Diamond"]

        # nested loop to get all card objs
        for rank in list_rank:
            for suit in list_suit:
                temp_value = 0
                if rank == "A":
                    temp_value = 1
                elif rank == "J" or rank == "Q" or rank == "K":
                    temp_value = 10
                else:
                    temp_value = int(rank)

                self.drawDeck.append(Card(rank, suit, temp_value))

    def shuffleDeck(self):
        random.shuffle(self.drawDeck)

    # debug printer
    def printDeck(self):
        for i in self.drawDeck:
            print(f"{i.rank} {i.suit} {i.value}")

class Gamestate():
    def __init__(self) -> None:
        pass

    def startGame(self):
        d1 = Deck()
        d1.genDeck()
        # d1.printDeck() # debugger
        d1.shuffleDeck()
        t1 = Table(4, d1) # 4 can be change, this is number of players
        t1.genPlayers()
        t1.genPlayerHands()
        t1.genTable()

        # gonna b in runOneTurn
        t1.printTable()
        t1.printPlayerHands()

    def runOneTurn(self):
        pass


gameOn = True
game = Gamestate()
game.startGame()

while gameOn:
    game.runOneTurn()
    gameOn = False