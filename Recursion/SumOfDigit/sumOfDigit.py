def sumOfDigits(num):

    assert num>=0 and int(num) == num , "The Number has to be a positive integer"

    if num == 0:
        return num

    else:
        return num%10 + sumOfDigits(num//10)


user_input = int(input("Enter number: "))
print(sumOfDigits(user_input))