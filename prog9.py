number = int(input("Enter the number : "))
flag = 0
if number > 0 :
    for x in range(number-1, 2, -1) :
        if number % x == 0:
            flag = 1
    if flag == 1 :
        print(number, "is not a prime number.")
    else :
        print(number, "is a prime number.")
elif number == 0 or number < 0:
    print(number, " is neither prime nor composite.")
