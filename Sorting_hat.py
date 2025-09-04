#Task from CodeDex.

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0 

#Question 1

print("Q1) Do you like Dawn or Dusk?\n"
"1) Dawn\n"
"2) Dusk")
ans=(int(input("Answer: ")))

if ans == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif ans == 2:
    Hufflepuff = Hufflepuff + 1
    Slytherin = Slytherin + 1
else:print("Wrong Input")  

#Question 2

print("Q2) When I’m dead, I want people to remember me as\n"
    "1) The Good\n"
    "2) The Great\n"
    "3) The Wise\n"
    "4) The Bold")
ans = (int(input("Answer: ")))

if ans == 1:
    Hufflepuff = Hufflepuff + 2
elif ans == 2:
    Slytherin = Slytherin + 2
elif ans == 3:
    Ravenclaw = Ravenclaw + 2
elif ans == 4:
    Gryffindor = Gryffindor + 2
else: print("Wrong input") 

#Question 3

print("Q3) Which kind of instrument most pleases your ear?\n"
    "1) The violin\n"
    "2) The trumpet\n"
    "3) The piano\n"
    "4) The drum")
ans = (int(input("Answer: ")))

if ans == 1:
    Slytherin = Slytherin + 4
elif ans == 2:
    Hufflepuff = Hufflepuff + 4
elif ans == 3:
    Ravenclaw = Ravenclaw + 4
elif ans == 4:
    Gryffindor = Gryffindor + 4
else: print("Wrong input")

print("Total score of each house is: Ravenclaw:", Ravenclaw , "Slytherin:", Slytherin,  "Hufflepuff:", Hufflepuff, "Gryffindor:", Gryffindor)
