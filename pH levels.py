#Task: Calcule pH of the Liquids:
#Source: Codedex Python Practice
ph=int(input("Write the pH value of the substance(0-14): "))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else: print("Neutral")
