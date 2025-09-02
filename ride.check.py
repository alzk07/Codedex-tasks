#Task: Check if the user is eligible to ride.
#Source: Codedex python practice.

#Taking input.
height=(int(input("Please enter your height(cm)")))
credits=(int(input("Please enter your remaining credits"))) 

#Checking:
if height>137 and credits>10:
  print("Enjoy the ride")
elif height<137 and credits>10:
  print("You are not tall enough to ride.")
elif height>137 and credits<10:
  print("You don't have enough credits")
else:
  print("You have not met either requirements")
