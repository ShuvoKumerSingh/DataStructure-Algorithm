# Using Euclidean Algorithm
def decimalToBinary(num):
    assert int(num) == num, 'The parameter must be integer only'
    if num == 0:
        return 0
    else:
        return num%2 + decimalToBinary(num//2)*10



print("How to convert a number from Decimal to Binary")

user_inp = int(input("Enter  number: "))

print(decimalToBinary(user_inp))