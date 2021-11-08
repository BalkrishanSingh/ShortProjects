from BlackJack import continue_playing
from random import randint
hand = ['r','p','s']
computer = hand[randint(0,2)]
while True:
    try:
        player = input('input, r for rock, p for paper, s for scissor : ')
        if player.lower() not in ['r','p','s']:
            continue
    except:
        print('Invalid Input, Try Again')
        continue
    else:
        if player == computer:
            print('Its a Tie')

        elif player == 'r':
            if computer == 's':
                print('Player wins! Computer was scissor')
            elif computer == 'p':
                print('Computer wins! Computer was paper')


        elif player == 's':
            if computer == 'p':
                print('Player wins! Computer was paper')
            elif computer == 'r':
                print('Computer wins! Computer was rock')

        elif player == 'p':
            if computer == 'r':
                print('Player wins! Computer was rock')
            elif computer == 's':
                print('Computer wins! Computer was scissor')

    if continue_playing() == True:
        continue
    else:
        break
