# insertion sort in ascending order
def insertion_sort(list1):
    for i in range(len(list1)):
        pos = i
        while pos > 0 and list1[pos] < list1[pos-1]:
            list1[pos], list1[pos-1] = list1[pos-1], list1[pos]
            pos = pos - 1

    for i in range(len(list1)):
        print(list1[i], end=' ')


A = [4, 3, 7, 5, 6, 9, 8, 2]
insertion_sort(A)
print()
# insertion sort descending order
def insertion_sort(list1):
    for i in range(len(list1)):
        pos = i
        while pos > 0 and list1[pos] > list1[pos-1]:
            list1[pos], list1[pos-1] = list1[pos-1], list1[pos]
            pos -= 1
    for i in range(len(list1)):
        print(list1[i], end=" ")


A = [4, 3, 7, 5, 6, 9, 8, 2]
insertion_sort(A)
