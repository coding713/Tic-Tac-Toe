def playmove():
    board = "7|8|9\n-----\n4|5|6\n-----\n1|2|3"
    playerOerror = 0
    while True:
        confirm = input("If you wanna play TicTacToe type 'start' \n")
        if confirm.upper() == "START":
            print(board)
            while True:
                if playerOerror == 0:
                    playerX = input("What is your move? Type the number of the position, Player X ")
                    if playerX.isdigit() and 0<int(playerX)<10:  
                        for x in board:
                            if playerX == x:
                                board = board.replace(x, 'X')
                                print(board)
                        if board[0:5] == "X|X|X" or board[12:17] == "X|X|X" or board[24:29] == "X|X|X":
                            print("Player X has won")
                            print(board)
                            break
                        elif board[0] =='X' and board[12] == 'X' and board[24] == 'X':
                            print("Player X has won")
                            print(board)
                            break
                        elif board[2] == 'X' and board[14] == 'X' and board[26] == 'X':
                            print("Player X has won")
                            print(board)
                            break
                        elif board[4] == 'X' and board[16] == 'X' and board[28] == 'X':
                            print("Player X has won")
                            print(board)
                            break
                        elif board[0] == 'X' and board[14] == 'X' and board[28] == 'X':
                            print("Player X has won")
                            print(board)
                            break
                        elif board[24] == 'X' and board[14] == 'X' and board[4] == 'X':
                            print("Player X has won")
                            print(board)
                            break
                        elif board.count('X') == 5:
                            print("Game is a draw")
                            break
                    else:
                        continue 
                else:
                    pass
                playerO = input("What is your move? Type the number of the position, Player O ")
                if playerO.isdigit() and 0<int(playerO)<10:
                    playerOerror = 0 
                    for x in board:
                        if playerO == x:
                            board = board.replace(x, 'O')
                            print(board)
                    if board[0:5] == "O|O|O" or board[12:17] == "O|O|O" or board[24:29] == "O|O|O":
                        print("Player O has won")
                        print(board)
                        break
                    elif board[0] =='O' and board[12] == 'O' and board[24] == 'O':
                        print("Player O has won")
                        print(board)
                        break
                    elif board[2] == 'O' and board[14] == 'O' and board[26] == 'O':
                        print("Player O has won")
                        print(board)
                        break
                    elif board[4] == 'O' and board[16] == 'O' and board[28] == 'O':
                        print("Player O has won")
                        print(board)
                        break
                    elif board[0] == 'O' and board[14] == 'O' and board[28] == 'O':
                        print("Player O has won")
                        print(board)
                        break
                    elif board[24] == 'O' and board[14] == 'O' and board[4] == 'O':
                        print("Player O has won")
                        print(board)
                        break
                else:
                    playerOerror = 1
        else:
            break 
playmove()
