# find duplicate number in list
def duplicate(ls):
    size = len(ls)
    for i in range(0, size):
        for j in range(i+1, size):
            if ls[i] == ls[j]:
                print(ls[i], end=" ")


ls = [1, 8, 3, 4, 5, 5, 7, 8, 4, 7, 9, 9]
duplicate(ls)
