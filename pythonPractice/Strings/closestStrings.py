
'''Find the minimum distance between the given two words
Examples:
    Input: S = { “the”, “quick”, “brown”, “fox”, “quick”}, word1 = “the”, word2 = “fox”
    Output: 3
    Explanation: Minimum distance between the words “the” and “fox” is 3'''
def shortestDistance(S, word1, word2):
    d1 = -1
    d2 = -1
    ans = 1000000
    for i in range(len(S)):
        if (S[i] == word1):
            d1 = i
        if (S[i] == word2):
            d2 = i
        if (d1 != -1 and d2 != -1):
            ans = min(ans, abs(d1 - d2))
    return ans

S = ["the", "quick", "brown", "fox", "quick"]

word1 = "the"
word2 = "fox"

# Function Call
print(shortestDistance(S, word1, word2))