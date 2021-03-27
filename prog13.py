number = int(input("Enter the number : "))
temp = number
finalNumber = 0
arr = []
for x in range(0, len(str(temp)), 1):
    lastNum = number % 10
    number = number // 10
    multiply = lastNum ** len(str(temp))
    finalNumber = finalNumber + multiply
if finalNumber == temp :
    print(temp, "is an Amstrong number")
else :
    print(temp, "is not an Amstrong number")