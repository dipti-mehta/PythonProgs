# take a string and check if that
# string contains atleast 1 digit and 1 letter
def isalnum(str1):
    is_letter = False
    is_digit = False
    for i in str1:
        if i.isalpha():
            is_letter = True

        if i.isdigit():
            is_digit = True

    return is_digit,is_letter

# driver code
print(isalnum('shraddha27'))
print(isalnum('shraddha'))