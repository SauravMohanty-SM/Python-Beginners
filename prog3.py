x = int(input("Enter the number : "))
factorial = 1
if x < 0 :
    print("Sorry, the factorial of -ve numbers does not exit.")
elif x == 0 :
    print("The factorial of 0 is 1")
else:
    for a in range(x, 1, -1):
        factorial = factorial*a
    print("The factorial of ", x, "is : ", factorial)