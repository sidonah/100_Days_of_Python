print (" welcom to lov calculator!")
name1= input("what is your name?")
name2= input("what is their name?")


combined_string= name1+name2
lower__Case_string= combined_string.lower()

t = lower__Case_string.count("t")
r = lower__Case_string.count("r")
u = lower__Case_string.count("u")
e = lower__Case_string.count("e")


true = t + r + u + e

l = lower__Case_string.count("l")
o = lower__Case_string.count("o")
v = lower__Case_string.count("v")
e = lower__Case_string.count("e")

love = l + o + v + e

love_score= int(str(true) + str(love))

# int_score=int(love_score)

if (love_score < 10 )or (love_score>90):
  print(f"your love score is {love_score}, you go together like coke and mentos")
  
elif (love_score >= 40) and (love_score <= 50):
   print(f"your  score is {love_score}, you are alright together ")
else:
    print(f"your score is {love_score}")