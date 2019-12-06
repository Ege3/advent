import math

fail = open("input.txt","r")
total = 0
for mass in fail:
    while math.floor(int(mass) / 3) - 2 > 0:
        fuel = math.floor(int(mass) / 3) - 2 
        total += fuel
        mass = fuel

print(total)    

fail.close()

