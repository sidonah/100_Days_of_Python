row1=["-","-","-"]
row2=["-","-","-"]
row3=["-","-","-"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put  the treeasure ")

horizontal= int(position[0]) #2
veertical = int (position[1])  #3
map[veertical-1][horizontal-1] = "X"
print(f"{row1}\n{row2}\n{row3}")