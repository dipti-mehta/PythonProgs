def longest_common_prefix(strs):
    if not strs:
        return "-1"

    strs.sort()
    first = strs[0]
    last = strs[-1]
    min_length = min(len(first), len(last))

    i = 0
    while i < min_length and first[i] == last[i]:
        i += 1

    if i == 0:
        return "-1"

    return first[:i]

strs = ["geeksforgeeks", "geeks", "geek", "geezer"]
print("The longest common prefix is:",
      longest_common_prefix(strs))