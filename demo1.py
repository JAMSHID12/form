list_value = [50, 20, 56, 63, 50]
def checkvalue():
    x = len(list_value)
    if list_value[0] == list_value[x - 1]:
        return True
    else:
        return False
    

t = checkvalue()
print(t)


