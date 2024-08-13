str1 = "geeksforgeeks"
str2 = "aaageekkuikss"
res = ""
for i in str1:
    if i in str2 and not i in res:
        res = res + i
print(res)