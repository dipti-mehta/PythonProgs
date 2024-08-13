# Least Frequent Character in String
string = "ajhxsiwcwcbwimkaxnnnnnlkxopowqx"
all_freq = {}
for i in string:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = min(all_freq, key = all_freq.get)
print(res)