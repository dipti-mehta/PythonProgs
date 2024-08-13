# kth smallest element
def ksmall(l1,n,k):
    l1.sort()
    print(l1)
    return l1[k-1]

l1=[76,23,45,12,54,9]
n = len(l1)
k = 2
print("kth smallest is ", ksmall(l1,n,k))