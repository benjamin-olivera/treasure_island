print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


first_dec = input("You arrive to the kong island choose ... left or right\n")
if first_dec.lower() == "left":
  print("you are in the right direction continue across the woods\n")
else:
  print("You fall into a hole. Game over\n")
  
second_dec = input("You are in front of a river would you like to swim or wait\n")  
if second_dec.lower() == "wait":
  print("You see a little boat,you will use it to cross the river\n")
else:
  print("You are attacked by a trout. Game over\n")
  
third_dec = input("You are on the other side of the river when some magic doors appear. Which door? Red, Blue, or Yellow?\n")
if third_dec.lower() == "yellow":
  print("You win take the gold!\n")
elif third_dec.lower() == "red":
  print("Burned by fire. Game over\n")
elif third_dec.lower() == "blue":
  print("Eaten by beasts. Game over\n")
else:
  print("Game over\n")