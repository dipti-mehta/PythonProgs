# Find a peak element which is not smaller than its neighbours
'''Example:
    Input: array[]= {5, 10, 20, 15}
    Output: 20
    Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.

    Input: array[] = {10, 20, 15, 2, 23, 90, 67}
    Output: 20 or 90
    Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.
'''
def findpeak(arr,n):
    if n == 1:
        return 0
    if (arr[0] >= arr[1]):
        return 0
    if (arr[n-1]>=arr[n-2]):
        return arr[n-1]
    for i in range(1, n - 1):
        if (arr[i] >= arr[i-1] and arr[i] >= arr[i+1]):
            return i

# driver code
arr = [10, 20, 15, 2, 23, 90, 67]
n = len(arr)
print("index of peak element is ", findpeak(arr,n))