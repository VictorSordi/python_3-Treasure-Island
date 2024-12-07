print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
direction = input(
    "You're at a cross road. Where do you want to go?\n  " "  Type 'left or 'right'\n")
if (direction == "Left" or direction == "left"):
    direction = input(
        "You've come to a lake. There is a island in the middle of the lake.\n " " Type 'wait' to wait for a boat. Type 'swin' to swin across\n")
    if (direction == "wait" or direction == "Wait"):
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors.\n " " One red, one yellow and one blue. Which colour do you choose?\n")
        if (door == "Yellow" or door == "yellow"):
            print("You find the Treasure, Congratulations, YOU WIN!")
        elif (door == "red" or door == "Red"):
            print("A rock fall on your head, you died, Game Over!")
        elif (door == "blue" or door == "Blue"):
            print("A Giant Snake eats you, you died, Game over!")
        else:
            print("You slipped and hit your head")
    elif (direction == "swin" or direction == "Swin"):
        print("You Drowned, you died, Game Over!")
    else:
        print("You slipped and hit your head")

elif (direction == "right" or direction == "Right"):
    print("You fell into a hole")
else:
    print("You slipped and hit your head")
