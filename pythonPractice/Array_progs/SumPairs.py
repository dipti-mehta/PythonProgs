# Find all Pairs Whose Sum is Equal to Given number in Python
def SumPairs(arr, TargetSum):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == TargetSum:
                pairs.append((arr[i], arr[j]))
    return pairs

arr = [1,2,3,4,5,6,7,8,9,10]
TargetSum = 12
print("all pairs are : ", SumPairs(arr, TargetSum))