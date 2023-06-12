import random
dict_cards = {}

list1 = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
list2 = ["Ace", "Hearts", "Spade", "Diamond"]
list_cards = []
for number in list1:
    for symbol in list2:
        symbol += number
        if number == "A":
            dict_cards[symbol] = 1
        if number.isdigit():
            # print(j)
            list_cards.append(symbol)
            dict_cards[symbol] = int(number)
        if number == "J" or number == "Q" or number == "K":
            dict_cards[symbol] = 10

# print(dict_cards)

random.shuffle(list_cards)
flag = True
# print(list_cards)
player_hand = []
computer_hand = []

player_bust = False
computer_bust = False
# player_hand.append(list_cards[0])
# list_cards.pop(0)


while flag:
    player_count = 0
    computer_count = 0
    if not player_hand and list_cards:
        # print("?")
        player_hand.append(list_cards[0])
        list_cards.pop(0)
    if not computer_hand and list_cards:
        # print("?")
        computer_hand.append(list_cards[0])
        list_cards.pop(0)
    for i in player_hand:
        player_count += dict_cards[i]

    for j in computer_hand:
        computer_count += dict_cards[j]

    print(f"player_hand: {player_hand}")
    print(f"player_count: {player_count}")
    print(f"computer_hand: {computer_hand}")
    print(f"computer_count: {computer_count}")
    # print(list_cards)
    if not player_bust:
        answer = input("hit or pass? (h/p)")

        if answer.lower() == "h":
            player_hand.append(list_cards[0])
            list_cards.pop(0)
    # else:
    #     pass
    if not computer_bust:
        if random.choice(["h", "p"]) == "h":
            computer_hand.append(list_cards[0])
            list_cards.pop(0)
            print("computer chose hit")
        else:
            print("computer chose pass")

    for i in player_hand:
        player_count += dict_cards[i]
    for i in computer_hand:
        computer_count += dict_cards[i]
        # not done but outline okay
    # print(player_count)
    # print(computer_count)
    # flag = False
    if player_count > 21:
        player_bust = True
    if computer_count > 21:
        computer_bust = True

    if player_bust and computer_bust:
        flag = False