# using replace() method
orig_str = "GeeksforGeeks"
new_str = orig_str.replace('e', '')
print("removed all occurences of e " + new_str)

new_str = orig_str.replace('s', '', 1)
print("removed first occurence of s " + new_str)

# alt approach
orig_stri = "geeksforgeeks"
new_stri = ""
for i in range(len(orig_stri)):
    # for removing 3rd element
    if i != 2:
        new_stri = new_stri + orig_stri[i]
print("new string is " + new_stri)

# alt approach using slicing
orig_stri = "geeksforgeeks"
# for removing index 2 char
new_stri = orig_stri[:2] + orig_stri[3:]
print("after slicing wala " + new_stri)


