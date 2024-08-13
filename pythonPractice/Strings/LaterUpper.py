# take a string and convert later half of string to uppercase
str1 = "shraddhamehta"
later_upper = ''
half_index = len(str1)//2
for index in range(len(str1)):
    if index >= half_index:
        later_upper = later_upper + str1[index].upper()
    else:
        later_upper = later_upper + str1[index]
print(later_upper)