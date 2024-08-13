# reverse words
str1 = "I am beautiful"
stack = str1.split()
revstr = []
while stack:
    revstr.append(stack.pop())
print(revstr)
print(' '.join(revstr))