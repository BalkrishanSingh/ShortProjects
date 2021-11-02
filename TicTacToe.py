
def display_board(board):

    print( '| '+ board[7] + ' | ' + board[8] +' | '+ board[9] + ' |')
    print('|---|---|---| ')
    print( '| '+ board[4] + ' | ' + board[5] +' | '+ board[6] + ' |')
    print('|---|---|---| ')
    print( '| '+ board[1] + ' | ' + board[2] +' | '+ board[3] + ' |')
def player_input():
    player1 = 'Yeah'
    while not player1.upper() in ['X','O']:
        player1 = input("Will Player 1 Like to Play As 'X' Or 'O':").upper()
        if player1 == 'X':
            player2 = 'O'
        elif player1 =='O':
            player2 = 'X'
        else:
            print ('Invalid Choice')
    return (player1,player2)
def marker_placer(board,player_marker,position):
    board[position] = player_marker
def win_condition(a,b,c,board,marker):
      if board[a] == board[b] == board[c] == marker:
            return True
def win_check(board,marker):
    if win_condition(1,2,3,board,marker) == True:
        return True
    elif win_condition(4,5,6,board,marker) == True:
        return True
    elif win_condition(7,8,9,board,marker) == True:
        return True
    elif win_condition(1,4,7,board,marker) == True:
        return True
    elif win_condition(2,5,8,board,marker) == True:
        return True
    elif win_condition(3,6,9,board,marker) == True:
        return True
    elif  win_condition(1,5,9,board,marker) == True:
        return True
    elif win_condition(3,5,7,board,marker) == True:
        return True
    else:
        return False
from random import choice
def random_choser():
    if choice([0,1]) == 1:
        return ' Player 1'
    else:
        return 'Player 2'
def check_space(board,position):
    if type(position) is not int:
        return False
    else:
        return board[position] == ' '
def check_fullboard(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    else:
        return True
def player_choice(board):
    position = 0
    while position not  in [1,2,3,4,5,6,7,8,9] or not check_space(board,position):
        try:
            position= int(input('Please Choose Your Positon from 1-9:'))
        except:
            print('Invalid Option')
            continue
        else:
            pass
    return position
def replay():
    replay_choice = 'ABC'
    while replay_choice.upper() not in ['Y','N'] :
        replay_choice = input('Replay?(Y Or N):')
        if replay_choice.upper() == 'Y':
            return True
        elif replay_choice.upper() == 'N':
            return False
        else:
            pass
def ready():
    ready_choice = 'ABC'
    while ready_choice.upper() not in ['Y','N'] :
        ready_choice = input('Ready?(Y Or N):')
        if ready_choice.upper() == 'Y':
            return True
        elif ready_choice.upper() == 'N':
            return False
        else:
            pass
def game():
    print("Welcome To Tic Tac Toe")

    while True:
        # Play the game
        ## SET UP GAME
        board = [' ']*10
        player1_marker, player2_marker = player_input()
        Turn = random_choser()
        print(Turn + ' will go first')
        if ready() == True:
            game_on =  True
        else:
            game_on = False
            break

        ## GAMEPLAY
        while game_on:
            ###Player 1 Turn
            if Turn == 'Player 1':
                #display board
                display_board(board)
                #Take Positon
                position = player_choice(board)
                #Put marker in positon
                marker_placer(board,player1_marker,position)

                if win_check(board,player1_marker):# Checkingx if player 1 wins

                    display_board(board)
                    print('Player 1 Has Won')
                    game_on = False
                else:
                    if check_fullboard(board): #Checking if Game has tied
                        clear_output
                        display_board(board)
                        print('Game Has Tied')
                        game_on = False
                        break
                    else:

                        Turn = 'Player 2'
            ### Player 2 Turn
            else:
                display_board(board)
                position = player_choice(board)
                marker_placer(board,player2_marker,position)
                if win_check(board,player2_marker):# Checking if player 2 wins

                    display_board(board)
                    print('Player 2 Has Won')
                    game_on = False
                else:
                    if check_fullboard(board): #Checking if Game has tied

                        display_board(board)
                        print('Game Has Tied')
                        game_on = False
                        break
                    else:
                        Turn = 'Player 1'

        if not replay():
            board = [' ']*10
            break
if __name__ == '__main__':
    game()
