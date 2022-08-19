import random

ladder = {2:23, 7:29, 22:41, 28:77, 30:32, 44:58, 54:69, 70:90, 80:98}
snake = {27:17, 35:15, 39:20, 59:39, 66:56, 76:63, 99:50}

pos1 = 0 # Player1
pos2 = 0 # Player2

def move(pos):
    dice = random.randint(1,6)
    print(f'\nDice number: {dice}')
    old_pos = pos
    pos +=  dice
    if pos > 100:
        pos = old_pos

    if pos in ladder:
        print('Climbing the ladder')
        pos = ladder[pos]
        print(f'Position: {pos}') 
    elif pos in snake:
        print('Bitten by Snake')
        pos = snake[pos]
        print(f'Position: {pos}')
    else:
        print(f'Position: {pos}')
        
    return pos

def start():
    global pos1, pos2
    while True:
        player1 = input("\nPlayer1 turn.\nEnter 'y' to roll dice: ")
        if player1 == "y":
            pos1 = move(pos1)
            if pos1 >= 100:
                print("\nPlayer1 wins!!!")
                print(f"Player2 is still at {pos2}\n")
                break

        player2 = input("\nPlayer2 turn.\nEnter 'y' to roll dice: ")
        if player2 == "y":
            pos2 = move(pos2)
            if pos2 >= 100:
                print("\nPlayer2 wins!!!")
                print(f"Player1 is still at {pos1}\n")
                break

        if player1 != "y" or player2 != "y":
            print("\nInvalid input. Please get out of the game\n")
            break

if __name__ == "__main__":
    start()