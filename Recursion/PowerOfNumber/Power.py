def power(n,exp):

    if exp is 0:
        return 1
    else:
        return n * power(n,exp-1)

print(power(2,4))