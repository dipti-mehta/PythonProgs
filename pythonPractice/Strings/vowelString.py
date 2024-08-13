# Python Program to Accept the Strings Which Contains all Vowels
def check(str11):
    vowels = "aeiou"
    for vowel in vowels:
        if all(vowel in str11.lower() for vowel in vowels):
            return "accepted"
        return "not accepted"


str1 = "abhsiueinjioyu"
print(check(str1))
