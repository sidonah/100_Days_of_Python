print ('''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************   
''')

print (" welcome to treasure island ")
print ("your mission s to find the treasure ")
choice1= input('your at a crossroad , wheere do you want to go? Type "left" or "right".\n')
if choice1=="left":
   choice2= input(' you have com to a lake, there is an island i the middle of the lake. type "wait" to wait for a bboat. type "swim" to swim accorss \n').lower()
   if choice2=="wait":
     choice3=input("you  arrived at the island unharmed. there is a house wth 3 doors. one red one yellow and one  blue , which color do you choose? \n").lower()
    
     if choice3=="red":
         print("it's a room full of fire. game over ")
     elif choice3=="yellow":
         print ("you hav found the treasure! You Win!")
     elif choice3== "blue":
         print ("you entered a room full of beasts . Game Over ")
     else:
         print ("you chose a door that does not exist")
   else:
       print("you got attacked by an angry trout , game over ")    
else:
 print(" you fell into a hole ,game over ")