# Python program to print even length words in a string
# Input: s = "This is a python language"
# Output: This is python language
#
# Input: s = "i am laxmi"
# Output: am

sentence = "I am beautiful"
no_space = sentence.split(" ")
# after this split no_space will look like
# no_space = ['I','am','beautiful']
# since we split it with space so it will
# split words wherever space encountered
for i in no_space:
    if len(i)%2 == 0:
        print(i)