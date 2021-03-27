FirstNumber = int(input("Enter the 1st number : "))
SecondNumber = int(input("Enter the second Number : "))

def find_gcd(a,b):
    gcd = 1
    for x in range(1,a+1):
        if a%x==0 and b%x==0:
           gcd = x
    return gcd

print('HCF of %d and %d is %d' %(FirstNumber, SecondNumber, find_gcd(FirstNumber, SecondNumber)))

lcm = FirstNumber * SecondNumber / find_gcd(FirstNumber, SecondNumber)
print('LCM of %d and %d is %d' %(FirstNumber, SecondNumber, lcm))