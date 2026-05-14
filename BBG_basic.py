print("Bomb Building & Gun")
import random
a= int(input("How many times you want to play? "))
print("If you want to quit in between simply type 5 and press enter")
print('Type "1" for Bomb, "2" for Building and "3" for Gun')
player_points,computer_points=0,0
for i in range(a):
    print("Computer is choosing...")
    c= random.randint(1,3)
    print("Computer has chosen\nNow your turn")
    b=int(input("Enter your choice: "))
    if b==1:
        player_choice= "Bomb"
    elif b==2:
        player_choice="Building"
    elif b==5:
        print("Exiting...\nDone")
        break
    else:
        player_choice="Gun"
    if c==1:
        computer_choice= "Bomb"
    elif c==2:
        computer_choice_="Building"
    else:
        computer_choice="Gun"
    print(f"You Choice: {player_choice} and Computer's Choice: {computer_choice}")
    if b==c:
        print("You both made the same the same choice!! Tie")
        player_points+=1
        computer_points+=1        
    elif b==1 and c==3 or b==2 and c==1 or b==3 and c==2:
        print("You Lost")
        computer_points+=1
    elif b==1 and c==2 or b==2 and c==3 or b==3 and c==1:
        print("You Won")
        player_points+=1
if i>0:
    print("Thank You for playing the game")
    print(f"Your Score {player_points}, Computer Score {computer_points}")
