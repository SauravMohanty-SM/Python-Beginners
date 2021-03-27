x = int(input("Enter the 1st number : "))
y = int(input("Enter the 2nd number : "))
operation = input("Enter what you want to do : ")
if operation == "+" :
    print("The addition is : {a}".format(a = x+y))
elif operation == "*" :
    print("The addition is : {a}".format(a = x*y))
elif operation == "/" :
    print("The addition is : {a}".format(a = x/y))
elif operation == "-" :
    print("The addition is : {a}".format(a = x-y))
elif operation == "%" :
    print("The addition is : {a}".format(a = x%y))
else:
    print("You enter the wrong operation")