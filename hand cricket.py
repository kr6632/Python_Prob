import random
list=[1,2,3,4,5,6,7,8,9,0]
toss=['odd','even']
while True:
    u=input("Toss \n")
    if u=='odd':
        cu='even'
        print(cu)
    elif u=='even':
        cu='odd'
        print(cu)
    else:
        print('invalid input retry')
        continue
    n=int(input("number:"))
    c=random.choice(list[:-1])
    print(c)
    if (n+c)%2==0:
        if cu=='even':
            print('Computer wins')
            print('computer will bat')
        elif u=='even':
            print('You win')
            print('You will bat')
    else:
        if cu=='odd':
            print('Computer wins')
            print('Computer will bat')
        elif u=='odd':
            print("You win")
            print('You will bat')

    def play_hand_cricket():
        print("Welcome to Hand Cricket!")
        player_score = 0
        computer_score = 0
        while True:
            player_choice = int(input("Enter your choice (1-6): "))
            if player_choice < 1 or player_choice > 6:
                print("Invalid choice. Try again.")
                continue
            computer_choice = random.randint(1, 6)
            print("Computer's choice:", computer_choice)
            if player_choice == computer_choice:
                print("Out!")
                print("Your score:", player_score)
                break
            player_score += player_choice
            print("Your score:", player_score)
            computer_score = random.randint(1, player_score)
            print("Computer's score:", computer_score)
            if computer_score < player_score:
                print("You win!")
            elif computer_score > player_score:
                print("Computer wins!")
            else:
                print("wieket")
    play_hand_cricket()
    


