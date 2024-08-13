# take a sentence as string
# and capitalize the first and last
# character of each word from that sentence
str1 = "hello today is wonderful day"
str2 = str1.split(" ")
print(str2)
newstr = []
for i in str2:
    up = i[0].upper()+i[1:-1]+i[-1].upper()
    newstr.append(up)
print(' '.join(newstr))
