filename=open("C:\\...\\2019day1.txt", "r") 
spacecraftMod = filename.read().splitlines()
spacecraftMod = [int(i) for i in spacecraftMod]

# part 1
fuelReq = 0

for mass in spacecraftMod:
    fuelReq += (mass//3)-2
    
print("Sum of the fuel requirements for all the modules: ",fuelReq)

# part 1 with a function

def fuel(mass):
    return (mass // 3) - 2

fuelSum = 0
for i in spacecraftMod:
    fuelSum += fuel(i)
   
print("Sum of the fuel requirements for all the modules: ",fuelSum)

# part 2, recursion
def fuelRecursive(mass):
    remainingMass = fuel(mass)
    if remainingMass <= 0:
        return 0
    else:
        return remainingMass + fuelRecursive(remainingMass)

fuelRecursiveSum=0

for i in spacecraftMod:
   fuelRecursiveSum += fuelRecursive(i)

print("Recursive sum of the fuel requirements for all the modules: ",fuelRecursiveSum)
