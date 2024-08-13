def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [1, 8, 9, 6, 67, 45, 90, 234, 8, 45]
n = len(arr)
print(largest(arr, n))
