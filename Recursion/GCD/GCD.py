# Using Euclidean Algorithm
def gcd(a,b):
    assert int(a) == a and int(b) == b, 'The number must be integer only'
    # if the number is negative then it's convert negative numbers to positive.
    # First two if condition section...
    if a<0:
        a = -1 * a
    if b<0:
        b = -1 * b

    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print("How to find Greatest Common Divisor between two numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter sceond number: "))

print(gcd(num1,num2))