str1 = "I am beautiful"
# stack = []
stack = str1.split()
rev_str = []
# for word in str1.split():
#     stack.append(word)
print(stack)

while stack:
    rev_str.append(stack.pop())
print(rev_str)
rev_str = ' '.join(rev_str)
print(rev_str)