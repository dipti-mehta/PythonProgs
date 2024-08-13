str1 = "geeksforgeeks"
p = ""
for i in str1:
    if i not in p:
        p = p+i
print(p)