# print dupes from array

n = int(input("enter size of array"))
arr = []
for i in range(n):
    print(" Enter array element: ")
    arr.append(int(input()))
print(arr)
seen = set()
dupes = []
for item in arr:
    if item in seen:
        dupes.append(item)
    else:
        seen.add(item)
print("duplicate items are : ", dupes)
