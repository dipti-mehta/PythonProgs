str1 = "hello good morning"
str2 = str1.split()
new1 = []
print(str2)
for i in str2:
    new1.append(i[::-1])
print(' '.join(new1))
