def  productOfArray(arr):
    if len(arr)==1:
        return arr[0]
    else:
        return arr[-1]* productOfArray(arr[:-1])