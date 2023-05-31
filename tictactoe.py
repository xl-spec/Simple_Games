list_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def printer():
    print(
        f"{list_pos[0]} {list_pos[1]} {list_pos[2]}\n"
        f"{list_pos[3]} {list_pos[4]} {list_pos[5]}\n"
        f"{list_pos[6]} {list_pos[7]} {list_pos[8]}\n"
    )


def checkwin(flag2):
    if list_pos[0] == "x" and list_pos[1] == "x" and list_pos[2] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[3] == "x" and list_pos[4] == "x" and list_pos[5] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[6] == "x" and list_pos[7] == "x" and list_pos[8] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[0] == "x" and list_pos[3] == "x" and list_pos[6] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[1] == "x" and list_pos[4] == "x" and list_pos[7] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[2] == "x" and list_pos[5] == "x" and list_pos[8] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[0] == "x" and list_pos[4] == "x" and list_pos[8] == "x":
        print("Player X wins")
        flag2 = False
    if list_pos[6] == "x" and list_pos[4] == "x" and list_pos[2] == "x":
        print("Player X wins")
        flag2 = False

    if list_pos[0] == "o" and list_pos[1] == "o" and list_pos[2] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[3] == "o" and list_pos[4] == "o" and list_pos[5] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[6] == "o" and list_pos[7] == "o" and list_pos[8] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[0] == "o" and list_pos[3] == "o" and list_pos[6] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[1] == "o" and list_pos[4] == "o" and list_pos[7] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[2] == "o" and list_pos[5] == "o" and list_pos[8] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[0] == "o" and list_pos[4] == "o" and list_pos[8] == "o":
        print("Player o wins")
        flag2 = False
    if list_pos[6] == "o" and list_pos[4] == "o" and list_pos[2] == "o":
        print("Player o wins")
        flag2 = False

    return flag2


turns = 0
flag = True
while flag:
    printer()

    answer = input()

    if turns % 2 == 0:
        for j in range(len(list_pos)):
            if str(list_pos[j]) == answer:
                list_pos[j] = "x"
                turns += 1

    elif turns % 2 == 1:
        for j in range(len(list_pos)):
            if str(list_pos[j]) == answer:
                list_pos[j] = "o"
                turns += 1

    if checkwin(flag) == True:
        pass
    if checkwin(flag) == False:
        flag = False
    print(f"turn is {turns}")
    if turns == 9:
        print("tie")
        flag = False

# determines even or odd
# if turns % 2 == 0:
#   print("even")

# elif turns % 2 == 1:
#   print("odd")
