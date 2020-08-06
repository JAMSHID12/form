def merge_sort(A, B):
    A.sort()
    B.sort()
    C = []
    m = len(A)
    n = len(B)
    i, j = 0, 0
    while i+j < m+n:
        if j == n:
            C.append(A[i])
            i = i + 1
        elif i == n:
            C.append(B[j])
            j += 1
        elif A[i] <= B[j]:
            C.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            C.append(B[j])
            j = j+1

    return C

a = [1, 5, 3, 7]
b = [2, 6, 4, 9]
c = merge_sort(a, b)
print(c)