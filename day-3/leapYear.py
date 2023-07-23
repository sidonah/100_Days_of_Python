year =int (input("whch yar do you wan to check?"))

if year % 4 ==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("Leap year")
        else :
            print ("not leap year")
    else:
        print ("leap year ")
        
else:
    print(" not a leap year ")