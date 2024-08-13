# using slicing method
def reverse(orig_list):
    new_list = orig_list[::-1]
    return new_list


orig_list = [1,2,3,4,5,6,7,8,9]
print(reverse(orig_list))

# ----------------------------------------------------------
# Using the Reversed() and Reverse() Built-In Function

lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))

# -------------------------------------------------------------
# Reversing a list using two-pointer approach
def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while (left < right):
        # Swap
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1

    return arr

arr = [1, 2, 3, 4, 5, 6, 7]
print(reverse_list(arr))

# ----------------------------------------
# using insert function reverse a list
# input list
lst = [10, 11, 12, 13, 14, 15]
# the above input can also be given as
# lst=list(map(int,input().split()))
l = []  # empty list

# iterate to reverse the list
for i in lst:
    # reversing the list
    l.insert(0, i)
# printing result
print(l)
