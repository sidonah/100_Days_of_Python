print("welcome to th rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0
if height>= 120:
    print("you can ride the rollercoaster!")
    age = int (input("what is your age ?"))
    if age < 12:
        bill =5
        print("child tickts are $5.")
    elif age <= 18:
        bill=7
        print("your tiicket is $7.")
    elif age >= 45 and age <= 55:
        print("veerything is going to be okay.hav a  free ride on us .")
    else:
        bill=12
        print("please pay $12.")    
    
    wants_photo= input("do you want your photo taken ? Y or N  ?")
    if wants_photo == "Y":
     bill+= 3
    
    print (f"your final bill is ${bill}")
else:
    print("sorry, you have to grow taller before you can ride.")
        
    
    