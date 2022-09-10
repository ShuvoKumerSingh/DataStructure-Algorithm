def factorial(n):
    assert n>=1 and int(n) == n, "please give the integer number and 0 i not given"
    if n in [0,1]:
        return 1
    else:
        return (n*factorial(n-1))
result = factorial(4)
print(result)