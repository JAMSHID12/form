# Selection sort Asending order
def sorting(list1):
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]

    for i in range(len(list1)):
        print(list1[i] , end=" ")


A = [3, 5, 2, 7, 4, 9, 8]
sorting(A)
print()

# Selection sort Descending order
def sorting(list1):
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            if list1[i] < list1[j]:  # will small changes in less than
                list1[i], list1[j] = list1[j], list1[i]

    for i in range(len(list1)):
        print(list1[i], end=" ")


A = [3, 5, 2, 7, 4, 9, 8]
sorting(A)
print()
# selection sort using while condition
def selection_sort(list1):
    i = 0
    while i < len(list1):
        j = i
        while j < len(list1):
            if list1[i] > list1[j]:
                list1[i], list1[j] = list1[j], list1[i]
            j += 1
        i += 1

    i = 0
    while i < len(list1):
        print(list1[i], end=" ")
        i += 1


A = [4, 5, 3, 8, 2, 1, 9, 7]
selection_sort(A)


