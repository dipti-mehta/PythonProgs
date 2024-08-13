str1 = "hello good morning"
str2 = str1.split()
str3 = []
print(str2)
for i in str2:
    str3.append(i[::-1])
print(' '.join(str3))

# -------------------for rotating words-------------------
s = "i like this program very much"
words = s.split(' ')
string = []
for word in words:
    string.insert(0, word)

print(" ".join(string))
