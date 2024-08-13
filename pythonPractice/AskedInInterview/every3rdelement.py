arr1 = [1, 8, 9, 6, 67, 45, 90, 234, 8, 45]
arr2 = arr1[::-1]
arr3 = []
print(arr2)
for i in range(0, len(arr2), 3):
    arr3.append(arr2[i])
print(arr3)