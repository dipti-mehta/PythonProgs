# common characters from both the string
str1 = 'aabcddekll12@'
str2 = 'bb2211@55k'
str3 = ''
for i in str1:
    if i in str2:
        str3 += i
print(str3)