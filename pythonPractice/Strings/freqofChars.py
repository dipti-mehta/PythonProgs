elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq = {}
for i in elements:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)