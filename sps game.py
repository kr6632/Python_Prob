import random

list=['stone','paper','scissor']
result={'Player':0,'Comp':0}

while True:
    n=input("Enter Your Choice:")
    if n=='end':
        print("Game Over")
        break
    if n=='score':
        print(f"Final Score: Player={result['Player']} Computer={result['Comp']}")
        continue
    c=random.choice(list[:-1])
    print('Computer Choice:',c)
    if n==c:
        print("it's Draw")
    elif(n=='stone'and c=='scissor')or(n=='paper'and c=='stone')or(n=='scissor'and c=='paper'):
        print("You win")
        result['Player']+=1
    else:
        print("Computer Wins")
        result['Comp']+=1
