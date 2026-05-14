import random
print("Lady, Tiger & Hunter")
a = int(input("How many times you want to play? "))
print("If you want to quit in between simply type 5 and press enter")
print('Type "1" for Lady, "2" for Tiger and "3" for Hunter')
player_points, computer_points = 0, 0
choices = {1: "Lady", 2: "Tiger", 3: "Hunter"}
for i in range(a):
    print("Computer is choosing...")
    c = random.randint(1, 3)
    print("Computer has chosen\nNow your turn")
    user_input = input("Enter your choice: ")
    b = int(user_input)
    if b == 5:
        print("Exiting...\nDone")
        break
    if b not in choices:
        print("Invalid choice!")
        continue
    player_choice = choices[b]
    computer_choice = choices[c]
    print(f"Your Choice: {player_choice} and Computer's Choice: {computer_choice}")
    if b == c:
        print("You both made the same choice!! Tie")
        player_points += 1
        computer_points += 1        
    elif (b == 1 and c == 3) or (b == 2 and c == 1) or (b == 3 and c == 2):
        print("You Won")
        player_points += 1
    else:
        print("You Lost")
        computer_points += 1
if i > 0:
    print("Thank You for playing the game")
    print(f"Your Score {player_points}, Computer Score {computer_points}")
