# Python3 program to find minimum
# (or maximum) element in an array

# Minimum Function
def getMin(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = min(res, arr[i])
    return res

# Maximum Function
def getMax(arr, n):
    res = arr[0]
    for i in range(1,n):
        res = max(res, arr[i])
    return res

# Driver Program
arr = [12, 1234, 45, 67, 1]
n = len(arr)
print ("Minimum element of array:", getMin(arr, n))
print ("Maximum element of array:", getMax(arr, n))

# -----------approach 2-------------------------
arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]
print(f"largest element in array is {largest}")
print(f"smallest element in array is {smallest}")