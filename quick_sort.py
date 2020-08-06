def partition(A, l, r):
    i = l - 1
    piv = A[r]
    for j in range(l, r):
        if A[j] <= piv:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1
def quick_sort(A, l, r):
    if l< r:
        pi = partition(A,l,r)
        quick_sort(A, l, pi-1)
        quick_sort(A, pi+1, r)

a = [43, 32, 23, 10, 56, 78, 13]
n = len(a)
c = []
partition(a, 0, n -1)
for i in range(len(a)):
    if n - 1 == i:
        c.insert(n//2, a[i])
        break
    c.append(a[i])
print(c)
