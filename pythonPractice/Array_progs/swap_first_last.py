#swap firs and last element using third var temp
def swapfunc(list1):
    size = len(new_list)
    temp = list1[0]
    list1[0] = list1[size - 1]
    list1[size - 1] = temp
    return list1


new_list = [1,2,3,4,5,6,7,8,9]
print("orig list is", new_list)
print("swapped list is", swapfunc(new_list))

# using slicing method----------------------------------------------

def swapfunc2(list1):
    list1[0], list1[-1] = list1[-1], list1[0]
    return list1

new_list = [1,2,3,4,5,6,7,8,9]
print("orig list is", new_list)
print("swapped list is", swapfunc2(new_list))

# ------------------------------------------------------------
# 3rd approach
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
    start, *middle, end = list
    list = [end, *middle, start]

    return list


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))


