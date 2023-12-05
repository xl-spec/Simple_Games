mob_pos = [3, 4]
player_pos = [0, 0]
all_cord = []

def gridPrint():
    for i in range(0, 20):
        for j in range(0, 20):
            temp_cord = [i, j]

            if player_pos == temp_cord:
                print('p', end = '   ')  
            elif mob_pos == temp_cord:
                print('m', end = '   ')
            
            else:
                print('-', end='   ')
        print('\n')

gameOn = True
while gameOn:
    gridPrint()
    choice = input()
    if choice == "w":
        player_pos[0] -= 1
    elif choice == "s":
        player_pos[0] += 1
    elif choice == "a":
        player_pos[1] -= 1
    elif choice == "d":
        player_pos[1] += 1

        