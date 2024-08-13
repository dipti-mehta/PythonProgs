# swap 2 given elements from a list 1st approach

def swapped_list(listt, pos1, pos2):
    listt[pos1], listt[pos2] = listt[pos2], listt[pos1]
    return listt


list1 = [21,45,23,65,34,98]
pos1, pos2 = 1, 3
print("orig list is: ",list1)
print("swapped list is", swapped_list(list1,pos1-1,pos2-1))

# ------------------------------------------------------------------------------
# using one more approach
# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis


# Driver function
List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1-1, pos2-1))


