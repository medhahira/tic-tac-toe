import random

def computer_choice(i : int) -> int :
    return random.randint(0,i)

def print_table(table):
    print(table[1] + "|" + table[2] + "|" + table[3])
    print("-+-+-")
    print(table[4] + "|" + table[5] + "|" + table[6])
    print("-+-+-")
    print(table[7] + "|" + table[8] + "|" + table[9])

def check_win(table, user_choice, comp_choice):
    win = ""
    if table[1] == table[2] == table[3]:
        win = table[1]
    elif table[4] == table[5] == table[6]:
        win = table[4]
    elif table[7] == table[8] == table[9]:
        win = table[7]
    elif table[1] == table[4] == table[7]:
        win = table[1]
    elif table[2] == table[5] == table[8]:
        win = table[2]
    elif table[3] == table[6] == table[9]:
        win = table[3]
    elif table[1] == table[5] == table[9]:
        win = table[1]
    elif table[3] == table[5] == table[7]:
        win = table[3]

    if win == user_choice:
        return 1
    elif win == comp_choice:
        return 2
    else:
        return 0

board = {1: "1", 2: "2", 3: "3",
        4: "4", 5: "5", 6: "6",
        7: "7", 8:"8", 9: "9"}
board_idx = [0]*9
for i in board.keys():
    board_idx[i-1] = i

print("Welcome to the game of tic-tac-toe!!")
name_of_user = input("Enter your name here: ")
print(f"{name_of_user.title()} choose between the two: ")
print('1. "x" ')
print('2. "o" ')
choice_x_o = int(input("Enter the number corresponding to your choice: "))
while (choice_x_o!=1 and choice_x_o!=2):
    print("INVALID number entered")
    choice_x_o = int(input("Enter the number corresponding to your choice"))

if  choice_x_o == 1:
    user_choice = 'x'
    comp_choice = 'o'
elif choice_x_o == 2:
    comp_choice = 'x'
    user_choice = 'o'

#we always let the user go first:
print_table(board)

while(len(board_idx)!=0) and check_win(board, user_choice, comp_choice)==0: 
    print(f"{name_of_user.title()} choose the number of the place you want to place a {user_choice} on: ")
    user_number = int(input("enter: "))
    while(board[user_number] == "x" or board[user_number] == "o"):
        print("ERROR")
        print(f"{name_of_user.title()} choose the number of the place you want to place a {user_choice} on: ")
        user_number = int(input("enter: "))
    board[user_number] = user_choice
    board_idx.remove(user_number)
    if check_win(board, user_choice, comp_choice) == 1:
        print(f"{name_of_user.title()} won")
        break
    print_table(board)
    if len(board_idx) != 0 and check_win(board, user_choice, comp_choice)==0:
        n = len(board_idx)
        comp = computer_choice(n)
        board[board_idx[comp-1]] = comp_choice
        board_idx.remove(board_idx[comp-1])
        print_table(board)
        if check_win(board, user_choice, comp_choice) == 2:
            print("The computer won")
            break
    else:
        print("Game Ended")
        break
