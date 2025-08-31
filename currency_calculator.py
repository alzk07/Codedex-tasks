# Task: Convert and calculate the total money in USD.
# Source: Codédex Python Practice

Pesos=int(input("Enter the amount of money in pesos: "))
Soles=int(input("Enter the amount of money in soles: "))
Reais=int(input("Enter the amount of money in reais: "))

#conversion rates (approximate)
Pesos=Pesos*0.054
Soles=Soles*0.28
Reais=Reais*0.18

total=Pesos+Soles+Reais
print("The total leftover money in USD is",total)
