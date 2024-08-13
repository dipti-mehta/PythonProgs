def freq(arr,n,toFind):
    res = 0
    for i in range(n):
        if toFind == arr[i]:
            res += 1
    return res

arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
toFind = 2
print("frequency of 2 is ", freq(arr,n,toFind))