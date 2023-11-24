import random
import time
# uno

class GameState:
    def __init__(self, draw_list = []):
        self.draw_list = draw_list
        self.discard_list = []
        self.player_list = []
        self.turns = 0
        self.clockDirection = 1
        self.deckObj = Deck() 
        self.cardObj = Card()
        self.handObj = Hand()
        self.countPlayers = None
        self.totalCards = 0

    def startGame(self, 
                  countPlayers = None, 
                  countInitialCardsPerPlayer = None, 
                  countDigitCardsPerColor = None, 
                  countSpecialCardsPerColor = None, 
                  countWildCards = None):
        
        self.countPlayers = 4
        countPlayers = 4
        countInitialCardsPerPlayer = 7
        countDigitCardsPerColor = 2
        countSpecialCardsPerColor = 2
        countWildCards = 4

        self.initializeDeck(self.draw_list,
                            self.deckObj,
                            countDigitCardsPerColor, 
                            countSpecialCardsPerColor, 
                            countWildCards)

        self.initializePlayers(countPlayers, 
                               self.draw_list, 
                               countInitialCardsPerPlayer)
        
        self.makeDiscard(self.draw_list, self.discard_list)
        self.totalCards = len(self.draw_list)

    def makeDiscard(self, draw, discard):
        pickedCard = draw.pop()
        discard.append(pickedCard)
        while not pickedCard.effect == None:
            # this is to make sure that first card is normal
            print("re-do")
            # self.cardFace(self.draw)
            pickedCard = draw.pop()
            discard.append(pickedCard)

    def initializeDeck(self, deck, d1, digitN, specialN, wildN):
        d1.generateDeck(deck, digitN, specialN, wildN)
        d1.shuffleDeck(deck)
        
    def initializePlayers(self, playerN, deck, cardN):
        for num in range(playerN):
            self.player_list.append(Player(num))
            self.player_list[num].hand = []
            for _ in range(cardN):
                if len(deck) > 0:
                    currentCard = deck.pop()
                    self.player_list[num].hand.append(currentCard)
                else:
                    print("deck empty can't")

    def cardFace(self, pile):
        # whats at the top of the stack (end of a list)
        card = pile[-1]
        return self.cardObj.__str__(card)
    
    def isGameOver(self):
        for player in self.player_list:
            if not player.hand:
                print(f"winner: player {player.id}")
                
                return True
        return False
    
    def checkEffect(self):
        if self.discard_list[-1].used == False and self.discard_list[-1].effect != None:
            print("\n\nEFFECT\n\n")
            nextPos = self.turns + self.clockDirection
            nextPos %= self.countPlayers
            effect = self.handObj.giveEffect(self.discard_list[-1], self.player_list[nextPos])
            if effect == "s":
                self.turns += self.clockDirection
            elif effect == "r":
                self.clockDirection *= -1
            elif effect == "d":
                self.player_list[nextPos].hand.append(self.draw_list.pop())
                self.player_list[nextPos].hand.append(self.draw_list.pop())
                self.turns += self.clockDirection # no stacking
            elif effect == "w":
                newColor = random.choice(["red", "yellow", "blue", "green"])
                self.discard_list[-1].color = newColor
                print(f"Wild -> {newColor}")

                 # make sure next turn doesn't affect user
            self.discard_list[-1].used = True

    def deckChecKEmpty(self):
        if len(self.draw_list) <= 2:
            print("draw empty, shuffled discard becomes draw")

            tempFace = self.discard_list[-1]
            self.draw_list = self.discard_list[:-1]
            self.deckObj.shuffleDeck(self.draw_list)
            self.discard_list = [tempFace]

    def playerAction(self):
        playerTurnHand = self.player_list[self.turns].hand
        playerTurnPlay = self.handObj.findCard(playerTurnHand, self.discard_list[-1])
        print(f"player {self.turns}'s turn")

        if playerTurnPlay != "": # if matched
            print(f"Player {self.turns} plays {self.cardObj.__str__(self.player_list[self.turns].hand[playerTurnPlay])}")
            matchedCurrentCard = self.player_list[self.turns].hand.pop(playerTurnPlay)
            self.discard_list.append(matchedCurrentCard)
        else: # no matches
            currentCard = self.draw_list.pop()
            self.player_list[self.turns].hand.append(currentCard)

            playerTurnHand = self.player_list[self.turns].hand
            playerTurnPlay = self.handObj.findCard(playerTurnHand, self.discard_list[-1])
            print(f"Player {self.turns} draw one card: {self.cardObj.__str__(currentCard)}")

            if playerTurnPlay != "":
                print(f"Player {self.turns} plays drawn card: {self.cardObj.__str__(self.player_list[self.turns].hand[playerTurnPlay])}")
                self.player_list[self.turns].hand.pop()
                self.discard_list.append(currentCard)

    def updateTurns(self):    
        self.turns += self.clockDirection  
        self.turns %= self.countPlayers

    def runOneTurn(self):

        self.checkEffect()
        self.updateTurns()
        self.handObj.printAllHands(self.player_list, self.cardObj)
        print(f"Top Card: {self.cardFace(self.discard_list)}")
        self.deckChecKEmpty()                
        self.playerAction()
        print("")
        self.isGameOver()

class Player:
    def __init__(self, id, hand = None):
        self.id = id
        self.hand = hand

class Card:
    def __init__(self, color = None, number = None, effect = None, used = False):
        self.color = color
        self.number = number
        self.effect = effect
        self.used = used

    def __str__(self, card):
        if card.effect == "wild":
            return f"{card.effect} {card.color}"
        elif card.effect is None:
            return f"{card.number} {card.color}"
        else:
            return f"{card.effect} {card.color}"

class Deck():
    def __init__(self):
        self.cards = []
        
    def generateDeck(self, deck, digitN, specialN, wildN):
        color_list = ["red", "yellow", "blue", "green"]
        effect_list = ["skip", "reverse", "draw2"]
        currentColor = ""
        
        # makes 0-9 4-colored cards digitN times
        for _ in range(digitN):
            for col in range(0, 4): # colors
                for num in range(0, 10): # numbers
                    currentColor = color_list[col]
                    deck.append(Card(currentColor, num))

        # makes 12 unique colored cards one time
        for _ in range(specialN): # amount
            for col in range(4): # colors
                for uniq in range(3): # unique effect
                    currentColor = color_list[col]
                    deck.append(Card(currentColor, effect=effect_list[uniq]))

        # makes 4 wild cards one time
        for _ in range(wildN): 
            deck.append(Card(effect="wild"))
            
    def shuffleDeck(self, deck):
        random.shuffle(deck)

class Hand():
    def __init__(self) -> None:
        pass

    def printHand(self, player, cardObject):
        hand_list = []
        for card in player.hand:
            hand_list.append(cardObject.__str__(card))

        return hand_list
                
    def printAllHands(self, player_list, cardObject):
        for player in player_list:
            print(f"Player {player.id}'s hand: {self.printHand(player, cardObject)}")
            # self.printHand(player, cardObject)
    
    def findCard(self, player_hand, topCard):
        pos_found_card = []
        for i in range(len(player_hand)): # search for match
            if player_hand[i].color == topCard.color:
                pos_found_card.append(i)
            elif player_hand[i].number == topCard.number and topCard.number != None: # get rid of wild edge case
                pos_found_card.append(i)
            elif player_hand[i].effect == topCard.effect and topCard.effect != None:
                pos_found_card.append(i)
            elif player_hand[i].effect == "wild":
                pos_found_card.append(i)

        # temp printer
        hand_list = []
        for i in pos_found_card:
            card = player_hand[i]
            if card.effect is None:
                hand_list.append(f"{card.number} {card.color}")
            else:
                hand_list.append(f"{card.effect} {card.color}")
        ####

        print(hand_list)
        if len(pos_found_card) == 0:
            return ""
        else:
            return random.choice(pos_found_card)
        
    def giveEffect(self, playerSentCard, playerRecieve):
        if playerSentCard.effect == "skip":
            print("skipped")
            return "s"
        elif playerSentCard.effect == "reverse":
            print("reversing")
            return "r"
        elif playerSentCard.effect == "draw2":
            print(f"player {playerRecieve.id} draw 2")
            return "d"
        elif playerSentCard.effect == "wild":
            return "w"

game = GameState()
game.startGame()

print("boo")
while True:
    game.runOneTurn()
    # time.sleep(.02)
    if game.isGameOver() == True:
        break
    # input()
