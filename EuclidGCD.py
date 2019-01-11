# Find gcd for integers m and n
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Prompt the user to enter two integers
def main():
    a = eval(input("Please enter the first integer: "))
    b = eval(input("Pleae enter the second integer: "))
    print("The greatest common divisor for", m, "and", n, "is", gcd(m, n))

# Call the main function
main()
