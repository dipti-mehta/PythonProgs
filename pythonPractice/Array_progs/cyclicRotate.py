def rotate(arr1, n):
    i = 0
    j = n -1
    while(i != j):
        arr1[i], arr1[j] = arr1[j], arr1[i]
        i = i + 1
    pass

arr1 = [1,2,3,4,5]
n = len(arr1)
for i in range(0,n):
    print(arr1[i], end = " ")

rotate(arr1, n)

print()
for i in range(0,n):
    print(arr1[i], end = " ")