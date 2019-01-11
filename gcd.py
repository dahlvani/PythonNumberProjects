# Find gcd for integers a and b
def gcd(a, b):
    gcd = 1
    if a % b == 0:
        return b

    for k in range(int(n / 2), 0, -1):
        if a % k == 0 and b % k == 0:
            gcd = k
            break
    
    return gcd

# Prompt the user to enter two integers
def main():
    a = eval(input("Enter first integer: "))
    b = eval(input("Enter second integer: "))
    print("The greatest common divisor for", a, "and", b, "is", gcd(a, b))

#Call the main function
main()
