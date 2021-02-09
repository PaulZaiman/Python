from random import randint

game = ["rock", "paper", "siccor"]
computer = game[randint(0, 2)]

player = False
while player == False:
    player = input("rock, paper, siccor :")
    # בדיקה שהתוכנית אכן נותנת ערך רנדומלי למחשב
    print(player, computer)
    # הוספת תנאים למשחק
    if player == computer:
        print("DRAW!")
    elif player == 'rock':
        if computer == 'paper':
            print(f'you LOSE! {computer} covers {player}')
        else:
            print(f'you WIN! {player} smash {computer}')
    elif player == "paper":
        if computer == "siccor":
            print(f'you LOSE {computer} cuts {player}')
        else:
            print(f'you WIN! {player} covers {computer}')
    elif player == "siccor":
        if computer == "rock":
            print(f'you LOSE! {computer} smash {player}')
        else:
            print(f'you WIN {player} cuts {computer}')

    player = False
    computer = game [randint(0, 2)]
